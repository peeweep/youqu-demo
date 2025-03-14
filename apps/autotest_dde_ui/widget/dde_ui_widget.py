#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/14 15:53:09
"""

from apps.autotest_dde_ui.widget.base_widget import BaseWidget
from src import log


@log
class DdeUiWidget(BaseWidget):
    """应用方法主类"""

    def click_dde_control_center_on_dde_dock_by_attr(self):
        """点击任务栏上的控制中心图标(通过属性定位)"""
        self.dog.element_click("Btn_control center")

    def click_dde_file_manager_on_dde_dock_by_attr(self):
        """点击任务栏上的文件管理器图标(通过属性定位)"""
        self.dog.element_click("Btn_file manager")
