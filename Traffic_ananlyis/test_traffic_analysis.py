# -*- coding:UTF-8 -*-
import unittest
import sys
import os
import time
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GemstoneLib.page_class import para, login_page

class Test_suite_traffic(unittest.TestCase):
    def setUp(self):
        self.login = login_page()
        self.project_manager = self.login.open_browser_to_login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)

    def test_C571718(self):
        pass
        # task_name = str(int(time.time()))
        # project_navigation = self.project_manager.build_project(task_name)
        # Traffic_analysis = project_navigation.goto_traffic_analysis()
        # print Traffic_analysis.pacpstart()
        # self.project_manager.goto_project_manager()
        # self.project_manager.delete_project(task_name)

    def test_C571717(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        traffic_analysis.set_parameter(min='5', sec='10', size='5')
        traffic_analysis.start_intercept()
        time.sleep(10)
        traffic_analysis.stop_intercept()
        result1 = traffic_analysis.check_pcap()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result1)

    def test_C571715(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        traffic_analysis.set_parameter(hour='99', min='60', sec='60')
        result = traffic_analysis.intercept_disable()
        traffic_analysis.go_back()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C571724(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        traffic_analysis.set_parameter(hour='', min='5', sec='', size='1')
        traffic_analysis.start_intercept()
        time.sleep(320)
        result1 = traffic_analysis.check_pcap()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result1)

    def test_C736898(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        traffic_analysis.set_parameter(hour='', min='', sec='', size='0')
        traffic_analysis.start_intercept()
        time.sleep(60)
        traffic_analysis.stop_intercept()
        result1 = traffic_analysis.check_pcap()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result1)

    def test_C736878(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        traffic_analysis.set_parameter(hour='99', min='60', sec='60')
        result = traffic_analysis.intercept_disable()
        traffic_analysis.go_back()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C618049(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        traffic_analysis.start_intercept()
        time.sleep(5)
        traffic_analysis.goto_page('流量分析')
        project_navigation.goto_traffic_analysis()
        result = traffic_analysis.analysis_exist()
        traffic_analysis.go_back()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()          #关闭chrome浏览器
        time.sleep(3)

if __name__ =='__main__':
  unittest.main()