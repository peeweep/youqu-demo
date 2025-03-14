#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/14 15:53:09
"""
from apps.autotest_dde_ui.case import BaseCase
from apps.autotest_dde_ui.widget import DdeUiWidget
from src import sleep


class TestMyCase(BaseCase):

    def test_mycase_002(self):
        # 用例步骤，调用方法层封装好的方法进行操作
        DdeUiWidget().click_dde_control_center_on_dde_dock_by_attr()
        # 在关键节点进行断言
        # 等待 2 秒，判断终端是否启动
        sleep(2)
        self.assert_process_status(True, "dde-control-center")
