#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/15 14:56:18
"""
from apps.autotest_http.config import config
from src import Src


class BaseApi(Src):
    """应用的方法基类"""
    # 注意这里需要修改为应用的包名
    APP_NAME = "http"
    DESC = "/usr/bin/http"

    def __init__(self, number=-1, check_start=False):
        kwargs = {}
        if number == -1:
            kwargs["name"] = self.APP_NAME
            kwargs["description"] = self.DESC
            kwargs["check_start"] = check_start
            kwargs["config_path"] = config.UI_INI_PATH
        if number > 0:
            kwargs["number"] = number
        Src.__init__(self, **kwargs)
