#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/15 15:57:37
"""
from src.webui import WebUI


class BasePage(WebUI):

    def __init__(self, page):
        super().__init__(page)
