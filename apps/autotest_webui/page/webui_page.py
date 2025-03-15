#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/15 15:57:37
"""

from apps.autotest_webui.page.base_page import BasePage


class WebuiPage(BasePage):
    """应用方法主类"""

    def click_xxx_by_attr(self):
        """click xxx button by attribute"""
        self.dog.find_element_by_attr("xxx").click()
