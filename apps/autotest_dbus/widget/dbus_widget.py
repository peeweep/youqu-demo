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

    def get_user1000_uid(self):
        """获取 Testservice 返回值"""
        return self.user1000_obj.get_system_properties_value("Uid")
