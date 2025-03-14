#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/14 15:53:09
"""
from apps.autotest_dde_ui.dde_ui_assert import DdeUiAssert


class BaseCase(DdeUiAssert):
    """用例基类"""
    APP_NAME = "dde-ui"
