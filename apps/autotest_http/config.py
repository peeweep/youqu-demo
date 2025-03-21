#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/15 14:56:18
"""
from os.path import join
from os.path import dirname
from os.path import abspath

from src import logger
from setting.globalconfig import _GlobalConfig
from setting.globalconfig import GetCfg


class _Config(_GlobalConfig):
    """
    Application library configuration
    """

    class DirName:
        """根目录"""
        TAG = "tag"
        RES = "res"
        CASE = "case"
        WIDGET = "widget"

        class SubDirName:
            """二级目录"""
            OTHER_INI = "other.ini"
            ASSERT_RES = "assert_res"
            UI_INI = "ui.ini"
            PIC_RES = "pic_res"
            CASE_RES = "case_res"
            DDT_RES = "ddt"

    ABSOLUTE_BASE_PATH = dirname(abspath(__file__))
    # check application library relative path
    if ABSOLUTE_BASE_PATH.split("/")[-2] != "apps":
        raise EnvironmentError
    # autotest_xxx
    APPLICATION_NAME = ABSOLUTE_BASE_PATH.split("/")[-1]
    # 应用库项目根目录绝对路径
    BASE_PATH = join(_GlobalConfig.APPS_PATH, APPLICATION_NAME)
    # 根目录下各目录绝对路径
    CASE_PATH = join(BASE_PATH, DirName.CASE)
    TAG_PATH = join(BASE_PATH, DirName.TAG)
    WIDGET_PATH = join(BASE_PATH, DirName.WIDGET)
    RES_PATH = join(BASE_PATH, DirName.RES)

    ASSERT_RES_PATH = join(CASE_PATH, DirName.SubDirName.ASSERT_RES)
    # res 目录下子目录绝对路径
    OTHER_INI_PATH = join(WIDGET_PATH, DirName.SubDirName.OTHER_INI)
    UI_INI_PATH = join(WIDGET_PATH, DirName.SubDirName.UI_INI)
    PIC_RES_PATH = join(WIDGET_PATH, DirName.SubDirName.PIC_RES)
    CASE_RES_PATH = join(WIDGET_PATH, DirName.SubDirName.CASE_RES)
    DDT_PATH = join(WIDGET_PATH, DirName.SubDirName.DDT_RES)

    # config ini object
    CONFIG_FILE_PATH = join(BASE_PATH, "config.ini")
    cfg = GetCfg(CONFIG_FILE_PATH, "config")

    # config.ini
    # dep_cfg = GetCfg(f"{BASE_PATH}/control", "Depends")
    # basic_frame_tag = dep_cfg.get("autotest-basic-frame")

    # if _GlobalConfig.current_tag != basic_frame_tag:
    #     logger.error(
    #         "应用库与基础框架对应版本不一致!"
    #         f"YouQu版本为:{_GlobalConfig.current_tag}，应用库版本为:{basic_frame_tag}"
    #         "如需如果您确认当前使用的YouQu版本正确，请检查您的应用工程根目录下control文件"
    #         "记录的依赖的YouQu版本是否一致~"
    #     )


config = _Config()
