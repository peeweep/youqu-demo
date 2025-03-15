#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/15 14:56:18
"""
from apps.autotest_http.http_assert import HttpAssert
import requests, urllib3


class BaseCase(HttpAssert):
    """用例基类"""

    def login_by_api(self):
        # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        login_url = f'{self.server_domain}/api/login'
        # password = hashlib.sha512(password.encode()).hexdigest()
        data = {"username": self.name, "password": self.password}
        r = requests.post(login_url, json=data)
        return r.status_code, r.json()['msg']
