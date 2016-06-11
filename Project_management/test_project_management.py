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

    def test_C618917(self):
        task_name = str(int(time.time()))
        self.project_manager.build_project(task_name)
        self.project_manager.goto_project_manager()
        result = self.project_manager.check_area_default_name(task_name)
        self.assertTrue(result)

    def test_C747678(self):
        task_name = str(int(time.time()))
        self.project_manager.build_project(task_name)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)

    def test_C747679(self):
        self.project_manager.start_project()
        self.project_manager.cancel_build()
        self.project_manager.exit_build()
        title2 = self.project_manager.get_current_page()
        page2 = u'项目管理'
        self.assertTrue(page2 in title2)

    def test_C747681(self):
        task_name = str(int(time.time()))
        self.project_manager.build_multiarea_project(project_name=task_name, number_of_area=1, area_name=['123'])
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()         #关闭chrome浏览器

if __name__ == '__main__':
    unittest.main()