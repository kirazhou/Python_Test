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

    def test_C736897(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        res = traffic_analysis.intercept_disable()
        traffic_analysis.set_pcap_name('@#$%^&')
        res2 = traffic_analysis.intercept_disable()
        # print res, res2
        traffic_analysis.go_back()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(not res and res2)

    def test_C736888(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        traffic_analysis.set_parameter(min='1', size='1')
        traffic_analysis.start_intercept()
        time.sleep(70)
        res = traffic_analysis.check_pcap()
        traffic_analysis.go_back()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res)

    def test_C747684(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        traffic_analysis.set_parameter(min='5', size='1')
        traffic_analysis.start_intercept()
        time.sleep(3)
        traffic_analysis.stop_intercept()
        traffic_analysis.go_to_report()
        res = traffic_analysis.get_intercept_time()
        traffic_analysis.close_report()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res in [u'3',u'4',u'5'])

    def test_C747402(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        traffic_analysis.set_parameter(min='5', size='1')
        traffic_analysis.start_intercept()
        time.sleep(3)
        traffic_analysis.stop_intercept()
        traffic_analysis.go_to_report()
        res = traffic_analysis.get_intercept_time()
        traffic_analysis.close_report()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res in [u'3',u'4',u'5'])

    def test_C736886(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        traffic_analysis.set_parameter(min='5', sec='20')
        traffic_analysis.start_intercept()
        time.sleep(330)
        res = traffic_analysis.check_pcap()
        traffic_analysis.go_back()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res)

    def test_C736880(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        traffic_analysis.set_parameter(sec='20')
        traffic_analysis.set_pcap_name(task_name)
        traffic_analysis.start_intercept()
        time.sleep(30)
        res = traffic_analysis.check_pcap()
        res1 = traffic_analysis.check_pcap_name(task_name)
        traffic_analysis.go_back()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res and res1)

    def test_C736879(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        traffic_analysis.set_pcap_name(task_name)
        traffic_analysis.set_parameter(sec='2')
        traffic_analysis.start_intercept()
        time.sleep(10)
        traffic_analysis.start_setting()
        traffic_analysis.set_pcap_name(task_name)
        traffic_analysis.set_parameter(sec='2')
        traffic_analysis.start_intercept()
        text = traffic_analysis.get_error_msg()
        traffic_analysis.go_back()
        print text
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(u'数据包名称已存在' in text)

    def test_C747687(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        traffic_analysis.start_intercept()
        time.sleep(5)
        traffic_analysis.refresh_page()
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