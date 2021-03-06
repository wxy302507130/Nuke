# -*- coding: UTF-8 -*-
"""Add callback for wlf plugins."""

import os

import nuke
import nukescripts

import asset
import edit
import wlfui
import cgtwn
import orgnize
from wlf import csheet
from node import wlf_write_node, Last


def init():
    """Add callback for nuke init phase."""

    nuke.addBeforeRender(create_out_dirs, nodeClass='Write')


def menu():
    """Add callback for nuke menu phase."""

    nukescripts.addDropDataCallback(asset.dropdata_handler)

    nuke.addAutolabel(wlfui.custom_autolabel)

    nuke.addUpdateUI(_gizmo_to_group_update_ui)

    nuke.addOnCreate(lambda: edit.set_random_glcolor(nuke.thisNode()))

    nuke.addOnUserCreate(_gizmo_to_group_on_create)

    nuke.addOnScriptLoad(_add_root_info)
    nuke.addOnScriptLoad(_eval_proj_dir)
    nuke.addOnScriptLoad(cgtwn.on_load_callback)
    nuke.addOnScriptLoad(Last.on_load_callback)

    nuke.addOnScriptSave(_autoplace)
    nuke.addOnScriptSave(_enable_node)
    nuke.addOnScriptSave(_check_project)
    nuke.addOnScriptSave(_check_fps)
    nuke.addOnScriptSave(_lock_connections)
    nuke.addOnScriptSave(_jump_frame)
    nuke.addOnScriptSave(cgtwn.on_save_callback)

    nuke.addOnScriptClose(lambda: asset.DropFrameCheck().start())
    nuke.addOnScriptClose(asset.DropFrameCheck.show_dialog)
    nuke.addOnScriptClose(_send_to_render_dir)
    nuke.addOnScriptClose(_render_jpg)
    nuke.addOnScriptClose(cgtwn.on_close_callback)
    nuke.addOnScriptClose(_create_csheet)


def abort_modified(func):
    """(Decorator)Abort function when project has been modified."""

    def _func():
        if nuke.Root().modified():
            return False
        func()
    return _func


def _enable_node():
    if nuke.numvalue('preferences.wlf_enable_node', 0.0):
        enable_node('_enable_')


def enable_node(prefix='_'):
    """Enable all nodes with given prefix."""
    task = nuke.ProgressTask('启用节点')
    nodes = tuple(n for n in nuke.allNodes() if n.name().startswith(prefix))
    all_num = len(nodes)
    count = 0
    for n in nodes:
        task.setMessage(n.name())
        task.setProgress(count * 100 // all_num)
        n['disable'].setValue(False)
        count += 1


@abort_modified
def _create_csheet():
    if nuke.numvalue('preferences.wlf_create_csheet', 0.0):
        if nuke.value('root.name'):
            csheet.create_html_from_dir(os.path.join(
                nuke.value('root.project_directory'), 'images'))


def _eval_proj_dir():
    if nuke.numvalue('preferences.wlf_eval_proj_dir', 0.0):
        attr = 'root.project_directory'
        nuke.knob(attr, os.path.abspath(nuke.value(attr)).replace('\\', '/'))


def _check_project():
    project_directory = nuke.value('root.project_directory')
    if not project_directory:
        _name = nuke.value('root.name', '')
        if _name:
            _dir = os.path.dirname(_name)
            nuke.knob('root.project_directory', _dir)
            nuke.message('工程目录未设置, 已自动设为: {}'.format(_dir))
        else:
            nuke.message('工程目录未设置')
    # avoid ValueError of script_directory() when no root.name.
    elif project_directory == r"[python {os.path.abspath(os.path.join("\
        r"'D:/temp', nuke.value('root.name', ''), '../'"\
            r")).replace('\\', '/')}]":
        nuke.knob('root.project_directory',
                  r"[python {os.path.join("
                  r"nuke.value('root.name', ''), '../'"
                  r").replace('\\', '/')}]")


def _check_fps():
    default_fps = 30
    if os.path.basename(nuke.value('root.name')).startswith('SNJYW'):
        default_fps = 25
    fps = nuke.numvalue('root.fps')
    if fps != default_fps:
        nuke.message('当前fps: {}, 默认值: {}'.format(fps, default_fps))


def _lock_connections():
    if nuke.numvalue('preferences.wlf_lock_connections', 0.0):
        nuke.Root()['lock_connections'].setValue(1)
        nuke.Root().setModified(False)


def _jump_frame():
    if nuke.numvalue('preferences.wlf_jump_frame', 0.0):
        n = wlf_write_node()
        if n:
            nuke.frame(n['frame'].value())
            nuke.Root().setModified(False)


@abort_modified
def _send_to_render_dir():
    if nuke.numvalue('preferences.wlf_send_to_dir', 0.0):
        asset.sent_to_dir(
            unicode(nuke.value('preferences.wlf_render_dir'), 'UTF-8'))


@abort_modified
def _render_jpg():
    if nuke.numvalue('preferences.wlf_render_jpg', 0.0):
        n = wlf_write_node()
        if n:
            print('render_jpg: {}'.format(n.name()))
            n['bt_render_JPG'].execute()


def _gizmo_to_group_on_create():
    n = nuke.thisNode()
    if not nuke.numvalue('preferences.wlf_gizmo_to_group', 0.0):
        return

    if not isinstance(n, nuke.Gizmo):
        return

    # Avoid scripted gizmo.
    if nuke.knobChangeds.get(n.Class()):
        return

    n.addKnob(nuke.Text_Knob('wlf_gizmo_to_group'))


def _gizmo_to_group_update_ui():
    n = nuke.thisNode()
    _temp_knob_name = 'wlf_gizmo_to_group'
    _has_temp_knob = nuke.exists('{}.{}'.format(n.name(), _temp_knob_name))

    if _has_temp_knob:
        n = edit.gizmo_to_group(n)
        n.removeKnob(n[_temp_knob_name])
        n.removeKnob(n['User'])


def _autoplace():
    if nuke.numvalue('preferences.wlf_autoplace', 0.0) and nuke.Root().modified():
        if nuke.numvalue('preferences.wlf_autoplace_type', 0.0) == 0.0:
            orgnize.autoplace()
        else:
            map(nuke.autoplace, nuke.allNodes())


def _print_name():
    print(nuke.thisNode().name())


def _add_root_info():
    """add info to root.  """

    artist = nuke.value('preferences.wlf_artist', '')
    if not artist:
        return
    if not nuke.exists('root.wlf'):
        n = nuke.Root()
        k = nuke.Tab_Knob('wlf', '吾立方')
        k.setFlag(nuke.STARTLINE)
        n.addKnob(k)

        k = nuke.String_Knob('wlf_artist', '制作人')
        k.setFlag(nuke.STARTLINE)
        k.setValue(artist)
        n.addKnob(k)
    else:
        if nuke.exists('root.wlf_artist') and not nuke.value('root.wlf_artist', ''):
            nuke.knob('root.wlf_artist', artist)


def create_out_dirs():
    """Create this read node's output dir if need."""

    target_dir = os.path.dirname(nuke.filename(nuke.thisNode()))
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)
