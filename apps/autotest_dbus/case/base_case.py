#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/14 19:30:49
"""
from apps.autotest_dbus.dbus_assert import DbusAssert


class BaseCase(DbusAssert):
    """用例基类"""
    APP_NAME = "dbus"
