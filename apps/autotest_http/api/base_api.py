#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/15 14:56:18
"""
from apps.autotest_http.config import config
from src import Src
import requests, urllib3


class BaseApi(Src):
    """应用的方法基类"""

    def login_by_api(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        login_url = f'{self.server_domain}/api/login'
        # password = hashlib.sha512(password.encode()).hexdigest()
        data = {"username": self.name, "password": self.password}
        headers = self.get_base_headers(headers={})
        r = requests.post(login_url, json=data)
        return r.status_code, r.data

    def get_cookie_token(self):
        header = {'Cookie': self.cookie, 'X-XSRF-TOKEN': self.csrf_token}
        get_headers = self.get_base_headers(header)
        return get_headers

    def get_base_headers(self, headers):
        base_headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            "Content-Type": "application/json",
            "Origin": self.server_domain,
            'Host': self.host,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
        if headers != {}:
            for k, v in headers.items():
                base_headers[k] = v
        return base_headers
