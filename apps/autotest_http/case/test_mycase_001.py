#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/15 14:56:18
"""
from apps.autotest_http.case import BaseCase
from apps.autotest_http.widget import HttpWidget

class TestMyCase(BaseCase):

    def test_mycase_001(self):
        """this is my test case"""
        # 用例步骤，调用方法层封装好的方法进行操作
        HttpWidget().click_xxx_by_attr()
        # 在关键节点进行断言
        self.assert_true(True)
