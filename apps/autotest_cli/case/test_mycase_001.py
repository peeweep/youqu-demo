#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/15 14:25:12
"""
from apps.autotest_cli.case import BaseCase
from apps.autotest_cli.widget import CliWidget


class TestMyCase(BaseCase):

    def test_mycase_001(self):
        """使用 dd 命令创建文件"""
        filepath = "Desktop/1.doc"
        cmd = CliWidget()
        cmd.create_file_by_dd_cmd()
        self.assert_file_exist(f"~/{filepath}")
