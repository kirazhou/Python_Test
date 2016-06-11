# -*- coding:UTF-8 -*-
import unittest
import sys
import os
import time
import re
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GemstoneLib.page_class import para, login_page


class Test_suite_sys(unittest.TestCase):
    def setUp(self):
        self.login = login_page()
        self.project_manager = self.login.open_browser_to_login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)

    def test_C617975(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        system = project_navigation.goto_system_setup('版本信息')
        edtion = system.get_version('软件版本信息')
        vullib = system.get_version('漏洞库版本信息')
        devliv = system.get_version('设备库版本信息')
        viruslib = system.get_version('签名库版本信息')
        edtion_pattern ='[A-Z]{2}[0-9]+\.[0-9]+\.[0-9]+\.[0-9]{4}\([0-9]+\)'
        other_pattern = '[A-Z]{2}[0-9]+\.[0-9]+\.[0-9]+\.[0-9]{4}'
        result1 = re.match(edtion_pattern, edtion)
        result2 = re.match(other_pattern, vullib)
        result3 = re.match(other_pattern, devliv)
        result4 = re.match(other_pattern, viruslib)
        self.assertTrue(result1 and result2 and result3 and result4)

    def test_C581201(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        system = project_navigation.goto_system_setup('系统设置')
        system.change_system_ip('0.0.0.0')
        ip_0000 = system.check_error_msg()
        system.change_system_ip('224.0.0.0')
        ip_224000 = system.check_error_msg()
        system.change_system_ip('127.0.0.0')
        ip_127000 = system.check_error_msg()
        self.assertTrue(ip_0000 and ip_224000 and ip_127000)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()          #关闭chrome浏览器

if __name__ =='__main__':
  unittest.main()