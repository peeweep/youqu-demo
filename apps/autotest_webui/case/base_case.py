#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/15 15:57:37
"""
from apps.autotest_webui.webui_assert import WebuiAssert


class BaseCase(WebuiAssert):
    """用例基类"""
    APP_NAME = "webui"
