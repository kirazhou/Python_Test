# -*- coding:UTF-8 -*-
import unittest
import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GemstoneLib.page_class import para, login_page

class Test_suite_full(unittest.TestCase):
    def setUp(self):
        self.login = login_page()
        self.project_manager = self.login.open_browser_to_login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)

    def test_C595354(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()  #关闭chrome浏览器
        time.sleep(3)

if __name__ =='__main__':
  unittest.main()