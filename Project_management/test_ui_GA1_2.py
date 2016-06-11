# -*- coding:UTF-8 -*-
import unittest
import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GemstoneLib.page_class import para, login_page


class Test_suite_project(unittest.TestCase):
    def setUp(self):
        self.login = login_page()
        self.project_manager = self.login.open_browser_to_login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)

    def test_C707348(self):
        task_name = str(int(time.time()))
        self.project_manager.build_project(task_name)
        text = self.project_manager.get_modules()
        expectation = [u'基本信息', u'威胁分析', u'资产分析', u'流量分析', u'报告管理']
        # print expectation, text
        result = True
        for i in range(len(text)):
            if not expectation[i] in text[i]:
                result = False
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()         #关闭chrome浏览器

if __name__ == '__main__':
    unittest.main()