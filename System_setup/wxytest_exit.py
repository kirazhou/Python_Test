# -*- coding:UTF-8 -*-
import unittest
import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GemstoneLib.page_class import para, login_page


class Test_suite_management(unittest.TestCase):
    def setUp(self):
        self.login = login_page()
        self.project_manager = self.login.open_browser_to_login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)

    def test_exit(self):
        while True:
            self.project_manager.goto_system_setup('退出')
            time.sleep(5)
            self.project_manager.goto_system(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)

    def test_C571704(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.begin()
        first = threat_analysis.check_commit()
        threat_analysis.close_report()
        threat_analysis.fill_questionnaire(1)
        second = threat_analysis.check_commit()
        threat_analysis.close_report()
        self.assertTrue(second and not first)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()          #关闭chrome浏览器

if __name__ =='__main__':
  unittest.main()
