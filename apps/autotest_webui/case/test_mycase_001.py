#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/15 15:57:37
"""
from apps.autotest_webui.case import BaseCase
from apps.autotest_webui.widget import WebuiWidget

class TestMyCase(BaseCase):

    def test_mycase_001(self):
        """this is my test case"""
        # 用例步骤，调用方法层封装好的方法进行操作
        WebuiWidget().click_xxx_by_attr()
        # 在关键节点进行断言
        self.assert_true(True)
