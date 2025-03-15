#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/14 19:30:49
"""
from apps.autotest_dbus.config import config
from src import Src
from src import logger
from src import OcrTextRecognitionError
from src.dbus_utils import DbusUtils


class BaseWidget(Src):
    """应用的方法基类"""
    # 注意这里需要修改为应用的包名
    APP_NAME = "dbus-daemon"
    DESC = "/usr/bin/dbus-daemon"

    def __init__(self, number=-1, check_start=True):
        kwargs = {}
        if number == -1:
            kwargs["name"] = self.APP_NAME
            kwargs["description"] = self.DESC
            kwargs["check_start"] = check_start
            kwargs["config_path"] = config.UI_INI_PATH
        if number > 0:
            kwargs["number"] = number
        Src.__init__(self, **kwargs)

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
