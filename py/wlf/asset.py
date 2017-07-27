# -*- coding: UTF-8 -*-
"""Deal with assets and files in nuke."""

import locale
import os
import re
import threading
import time

import nuke

from .files import expand_frame, copy

__version__ = '0.2.12'
SYS_CODEC = locale.getdefaultlocale()[1]


class DropFrameCheck(threading.Thread):
    """Check drop frames and record on the node."""

    lock = threading.Semaphore(10)
    showed_files = []
    knob_name = 'dropframes'
    dropframes_dict = {}

    def __init__(self, node, prefix=('_',)):
        threading.Thread.__init__(self)
        self.daemon = True
        self._node = node
        self._prefix = prefix
        self._name = self._node.name()

    @property
    def knob_tcl_name(self):
        """Custom knob name."""
        if self._node:
            return '{}.{}'.format(self._node.name(), self.knob_name)

    def run(self):
        time.sleep(5)
        with self.lock:
            if self._name.startswith(self._prefix) \
                    or self._node['disable'].value():
                return
            self.record()

    def dropframe_ranges(self):
        """Return nuke framerange instance of dropframes."""
        ret = nuke.FrameRanges()
        if not self._node:
            return ret
        _filename = nuke.filename(self._node)
        if not _filename:
            return ret
        if expand_frame(_filename, 1) == _filename:
            if not os.path.isfile(_filename):
                ret = self._node.frameRange()
            return ret

        _read_framerange = xrange(
            self._node.firstFrame(), self._node.lastFrame() + 1)
        folder = os.path.dirname(_filename)
        _listdir = os.listdir(folder)
        for f in _read_framerange:
            _file = os.path.basename(expand_frame(_filename, f))
            if _file not in _listdir:
                ret.add([f])
        ret.compact()
        return ret

    def record(self):
        """Record dropframes on knob for futher use."""

        _dropframes = self.dropframe_ranges()

        def _warning():
            if str(_dropframes):
                nuke.warning('{}: [dropframes]{}'.format(
                    self._node.name(), _dropframes))
        if str(_dropframes) != str(self.dropframes_dict.get(self._node, nuke.FrameRanges())):
            self.dropframes_dict[self._node] = _dropframes
            nuke.executeInMainThread(_warning)

    @classmethod
    def show_dialog(cls, show_all=False):
        """Show all dropframes to user."""
        message = ''
        for n, dropframes in cls.dropframes_dict.items():
            filename = nuke.filename(n)
            if not show_all\
                    and filename in cls.showed_files:
                continue
            if dropframes:
                message += '<tr><td>{}</td><td>'\
                    '<span style=\"color:red\">{}</span></td></tr>'.format(
                        filename, dropframes)
                cls.showed_files.append(filename)

        if message:
            message = '<style>td{padding:8px;}</style>'\
                '<table>'\
                '<tr><th>素材</th><th>缺帧</th></tr>'\
                + message + \
                '</table>'
            nuke.message(message)


def sent_to_dir(dir_):
    """Send current working file to dir."""
    copy(nuke.value('root.name'), dir_)


def dropdata_handler(mime_type, data, from_dir=False):
    """Handling dropdata."""
    # print(mime_type, data)
    if mime_type != 'text/plain':
        return
    match = re.match(r'file:///([^/].*)', data)

    if os.path.isdir(data):
        _dirname = data.replace('\\', '/')
        for i in nuke.getFileNameList(_dirname):
            dropdata_handler(
                mime_type, '{}/{}'.format(_dirname, i), from_dir=True)
    elif os.path.basename(data).lower() == 'thumbs.db':
        pass
    elif match:
        data = match.group(1)
        return dropdata_handler(mime_type, data, from_dir=True)
    elif data.endswith('.fbx'):
        n = nuke.createNode(
            'Camera2',
            'read_from_file True '
            'frame_rate 25 '
            'suppress_dialog True '
            'label {'
            '导入的摄像机：\n'
            '[basename [value file]]\n}')
        n.setName('Camera_3DEnv_1')
        n['file'].fromUserText(data)
        if nuke.expression('{}.animated'.format(n.name())):
            n['read_from_file'].setValue(False)

        n = nuke.createNode('ReadGeo2')
        n['file'].fromUserText(data)
        n['all_objects'].setValue(True)
    elif data.endswith('.vf'):
        nuke.createNode(
            'Vectorfield',
            'vfield_file "{data}" '
            'file_type vf '
            'label {{[value this.vfield_file]}}'.format(data=data))
    elif data.endswith('.nk'):
        nuke.scriptReadFile(data)
    elif from_dir:
        n = nuke.createNode('Read', 'file "{}"'.format(data))
    else:
        return
    return True
