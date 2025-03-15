#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/15 14:25:12
"""

from setting import conf
from src import Src


class CliWidget(Src):
    """应用方法主类"""

    def create_file_by_dd_cmd(self):
        """使用 dd 命令创建文件"""
        filename = "1.doc"
        filesize = "1M"
        self.run_cmd(
            f"dd if=/dev/zero of=/home/{conf.USERNAME}/Desktop/{filename} bs={filesize} count=1"
        )
