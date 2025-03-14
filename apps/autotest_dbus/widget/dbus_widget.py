#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/14 19:30:49
"""

from apps.autotest_dbus.widget.base_widget import BaseWidget
from src import log


@log
class DbusWidget(BaseWidget):
    """应用方法主类"""

    def click_xxx_by_attr(self):
        """click xxx button by attribute"""
        self.dog.find_element_by_attr("xxx").click()
