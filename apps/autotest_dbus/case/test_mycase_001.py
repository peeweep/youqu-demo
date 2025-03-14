#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/14 19:30:49
"""
from apps.autotest_dbus.case import BaseCase
from apps.autotest_dbus.widget import DbusWidget

class TestMyCase(BaseCase):

    def test_mycase_001(self):
        """this is my test case"""
        # 用例步骤，调用方法层封装好的方法进行操作
        DbusWidget().click_xxx_by_attr()
        # 在关键节点进行断言
        self.assert_true(True)
