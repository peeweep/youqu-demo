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
    def testservice_obj(self) -> DbusUtils:
        """授权接口对象"""
        # dbus_name
        #     eg.com.deepin.daemon.Appearance
        # object_path
        #     eg./com/deepin/daemon/Appearance
        # interface
        #     eg.com.deepin.daemon.Appearance

        dbus_name = "com.deepin.daemon.Apps"
        object_path = "/com/deepin/daemon/Accounts"
        interface = "com.deepin.daemon.Accounts"
        lo = DbusUtils(
            dbus_name, object_path, interface
        )
        return lo
