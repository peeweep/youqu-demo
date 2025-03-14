#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/14 19:30:49
"""
from apps.autotest_dbus.case import BaseCase
from apps.autotest_dbus.widget import DbusWidget
from src import sleep

class TestMyCase(BaseCase):

    def test_mycase_002(self):
        """快捷键 ctrl + alt + t 启动终端"""
        # 用例步骤，调用方法层封装好的方法进行操作
        DbusWidget.ctrl_alt_t()
        # 在关键节点进行断言
        # 等待 2 秒，判断终端是否启动
        sleep(2)
        self.assert_process_status(True, "deepin-terminal")
