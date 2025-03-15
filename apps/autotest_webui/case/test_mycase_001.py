#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/15 15:57:37
"""

from apps.autotest_webui.case import BaseCase
from apps.autotest_webui.page.baidu import BaiDu


class TestMyCase(BaseCase):

    def test_mycase_001(self, page):
        """百度首页搜索 YouQu """

        browser = BaiDu(page)
        # 在浏览器访问百度首页
        browser.goto_baidu()
        # 点击搜索框
        browser.click_search_box()
        # 输入YouQu
        browser.input_keywords("YouQu")
        self.assert_locator()
