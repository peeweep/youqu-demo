#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/14 19:30:49
"""
from src import Src
from src.dbus_utils import DbusUtils


class BaseWidget(Src):
    """应用的方法基类"""

    @property
    def user1000_obj(self) -> DbusUtils:
        """授权接口对象"""
        dbus_name = "org.freedesktop.Accounts"
        object_path = "/org/freedesktop/Accounts/User1000"
        interface = "org.freedesktop.Accounts.User"
        lo = DbusUtils(
            dbus_name, object_path, interface
        )
        return lo
