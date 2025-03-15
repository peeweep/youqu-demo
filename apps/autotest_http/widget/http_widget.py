#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/15 14:56:18
"""

from apps.autotest_http.widget.base_widget import BaseWidget
from src import log


@log
class HttpWidget(BaseWidget):
    """应用方法主类"""

    def click_xxx_by_attr(self):
        """click xxx button by attribute"""
        self.dog.find_element_by_attr("xxx").click()
