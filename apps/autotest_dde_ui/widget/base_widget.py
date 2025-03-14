#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:youqu-user
:Date  :2025/03/14 15:53:09
"""
from apps.autotest_dde_ui.config import config
from src import Src
from src import logger
from src import OcrTextRecognitionError


class BaseWidget(Src):
    """应用的方法基类"""
    # 注意这里需要修改为应用的包名
    APP_NAME = "dde-dock"
    DESC = "/usr/bin/dde-dock"

    def __init__(self, number=-1, check_start=True):
        kwargs = {}
        if number == -1:
            kwargs["name"] = self.APP_NAME
            kwargs["description"] = self.DESC
            kwargs["check_start"] = check_start
            kwargs["config_path"] = config.UI_INI_PATH
        if number > 0:
            kwargs["number"] = number
        Src.__init__(self, **kwargs)

    @classmethod
    def find_image_in_screen(cls, *elements, rate=0.9, picture_abspath=None):
        """查找图片坐标"""
        element = tuple(map(lambda x: f"{config.PIC_RES_PATH}/{x}", elements))
        return cls.find_image(*element, rate=rate, picture_abspath=picture_abspath)

    def find_image_in_dde_ui(self, *elements, rate=0.9):
        """
         在应用窗口查找图片
        """
        # 窗口大小参数
        _x, _y, widget, height = self.ui.btn_size("窗口")
        pic = self.save_temporary_picture(_x, _y, widget, height) + ".png"
        result = self.find_image_in_screen(*elements, rate=rate, picture_abspath=pic)
        _x, _y = _x + result[0], _y + result[1]
        logger.info(f"坐标为 （{_x}, {_y}）")
        return _x, _y

    def ocr_in_window_by_ui(self, *target_strings, similarity=0.6, return_first=True, lang="ch"):
        """
         在应用窗口中识别文案
        """
        # 窗口大小参数
        _x, _y, widget, height = self.ui.btn_size("窗口")
        pic = self.save_temporary_picture(_x, _y, widget, height) + ".png"
        result = self.ocr(*target_strings, picture_abspath=pic, similarity=similarity, return_first=return_first, lang=lang)
        if result:
            _x, _y = _x + result[0], _y + result[1]
            logger.info(f"坐标为 （{_x}, {_y}）")
            return _x, _y
        raise OcrTextRecognitionError(str(target_strings))
