# -*- coding: UTF-8 -*-
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'py'))
import wlf
import nuke

nuke.pluginAddPath('plugins')
wlf.callback.init()
wlf.pref.set_knob_default()
# _dir = '//SERVER/scripts/NukePlugins/Fonts'
# if os.path.isdir(_dir):
    # os.environ['NUKE_FONT_PATH'] = _dir

