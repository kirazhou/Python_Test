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

    def test_C617974(self):
        # TODO: only check 0.0.0.0 for now.
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        system = project_navigation.goto_system_setup('无线设置')
        self.assertTrue(system.wifi_setup())

    def test_C581202(self):
        # TODO: only check LAN ip
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        system = project_navigation.goto_system_setup('系统设置')
        result1 = system.get_ip_infos()
        system.edit_ip_infos(['123.456.789','255.255.255.0','123.1456.123.1'])
        system.cancel_ip_edit()
        project_navigation.goto_system_setup('系统设置')
        result2 = system.get_ip_infos()
        system.cancel_ip_edit()
        page = system.get_current_page()
        # print result1, result2
        # print (result1 == result2), u'项目基本信息' in page
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue((result1 == result2) and u'项目基本信息' in page)

    def test_C757447(self):
        self.project_manager.goto_system_setup('账户管理')
        self.project_manager.goto_system_setup('日志管理')

    def tearDown(self):
        time.sleep(1)
        self.login.quit()          #关闭chrome浏览器

if __name__ =='__main__':
  unittest.main()