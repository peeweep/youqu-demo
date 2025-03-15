#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/15 14:56:18
"""
from apps.autotest_http.case import BaseCase


class TestMyCase(BaseCase):

    def test_mycase_001(self):
        """【接口测试-管理员】管理员登录"""
        # 接口请求管理员登录
        # 接口请求成功
        self.host = "localhost:5000"
        self.server_domain = "http://" + self.host + "/"
        self.name = "admin"
        self.password = "123456"
        status, content = self.login_by_api()
        self.assert_true((status == 200) & (content == "Login success"))

        # self.assert_api_response(
        #     actual_status=status,
        #     actual_content=content,
        #     expect_status=200,
        #     expect_code=0, expect_msg='Login success'
        # )
