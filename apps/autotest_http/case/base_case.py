#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/15 14:56:18
"""
from apps.autotest_http.http_assert import HttpAssert


class BaseCase(HttpAssert):
    """用例基类"""
    APP_NAME = "http"
