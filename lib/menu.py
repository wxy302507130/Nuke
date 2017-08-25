# -*- coding: UTF-8 -*-
"""Nuke menu file."""

import ui
import callback
import pref
from wlf import cgtwq

print(u'添加菜单')
ui.add_menu()
print(u'添加GUI callback')
callback.menu()
print(u'设置knob默认值')
pref.set_knob_default()
print(u'添加首选项面板')
pref.add_preferences()
if cgtwq.MODULE_ENABLE:
    print(u'更新CGTeamWork状态')
    cgtwq.CGTeamWork.update_status()
