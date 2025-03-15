from apps.autotest_webui.page.base_page import BasePage


class BaiDu(BasePage):

    def goto_baidu(self):
        """访问百度首页"""
        self.goto("http://www.baidu.com")

    def click_search_box(self):
        """点击搜索框"""
        self.page.locator("#kw").click()

    def input_keywords(self, keywords):
        """搜索框中输入关键词"""
        self.page.locator("#kw").fill(keywords)
