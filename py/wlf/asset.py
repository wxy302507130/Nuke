# -*- coding: UTF-8 -*-
"""Deal with assets and files in nuke."""

import locale
import os
import re
import threading

import nuke

from .files import expand_frame, copy

__version__ = '0.3.4'
OS_ENCODING = locale.getdefaultlocale()[1]


class DropFrameCheck(threading.Thread):
    """Check drop frames and record on the node."""

    showed_files = []
    dropframes_dict = {}

    def __init__(self, prefix=('_',)):
        threading.Thread.__init__(self)
        self.daemon = True
        self._prefix = prefix

    @property
    def knob_tcl_name(self):
        """Custom knob name."""
        if self._node:
            return '{}.{}'.format(self._node.name(), self.knob_name)

    def run(self):
        task = nuke.ProgressTask('检查缺帧')
        read_files = tuple((nuke.filename(n), n.frameRange())
                           for n in nuke.allNodes('Read') if not n['disable'].value())
        footages = {}
        for filename, framerange in read_files:
            footages.setdefault(filename, nuke.FrameRanges())
            footages[filename].add(framerange)
        dropframe_dict = {}
        all_num = len(footages)
        count = 0
        for filename, framerange in footages.items():
            if task.isCancelled():
                return
            framerange.compact()

            task.setMessage(filename)
            task.setProgress(count * 100 // all_num)
            dropframes = self.dropframe_ranges(
                filename, framerange.toFrameList())
            if str(dropframes):
                dropframe_dict[filename] = dropframes
                nuke.executeInMainThread(DropFrameCheck.show_dialog)

            count += 1
        DropFrameCheck.dropframes_dict = dropframe_dict

    @staticmethod
    def dropframe_ranges(filename, framerange):
        """Return nuke framerange instance of dropframes."""
        assert isinstance(framerange, (list, nuke.FrameRange))
        task = nuke.ProgressTask(u'验证文件')
        ret = nuke.FrameRanges()
        if expand_frame(filename, 1) == filename:
            if not os.path.isfile(unicode(filename).encode(OS_ENCODING)):
                ret.add(framerange)
            return ret

        folder = os.path.dirname(filename)
        if not os.path.isdir(folder):
            ret.add(framerange)
            return ret
        _listdir = list(unicode(i, OS_ENCODING) for i in os.listdir(folder))
        all_num = len(framerange)
        count = 0
        for f in framerange:
            task.setProgress(count * 100 // all_num)
            frame_file = unicode(os.path.basename(expand_frame(filename, f)))
            task.setMessage(frame_file)
            if frame_file not in _listdir:
                ret.add([f])
            count += 1
        ret.compact()
        return ret

    @classmethod
    def show_dialog(cls, show_all=False):
        """Show all dropframes to user."""
        message = ''
        for filename, dropframes in cls.dropframes_dict.items():
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
