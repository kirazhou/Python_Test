# -*- coding:UTF-8 -*-
import unittest
import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GemstoneLib.page_class import para, login_page


class Test_suite_project(unittest.TestCase):
    '''def setUp(self):
        self.login = login_page()
        self.project_manager = self.login.open_browser_to_login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)

    def test_C707384(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.auto_entry(scan_port=para.SCAN_PORT, ip_address=para.SCAN_SUBNET)
        asset.jump_to_threat(option='停止')
        log = project_navigation.goto_system_setup('日志管理')
        res1 = log.check_log_msg(project=task_name, msg='开始自动扫描')
        res2 = log.check_log_msg(project=task_name, msg='停止自动扫描')
        print res1, res2
        log.go_back()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res1 and res2)

    def test_C707385(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        traffic_analysis.set_parameter(sec='10')
        traffic_analysis.start_intercept()
        time.sleep(17)
        log = project_navigation.goto_system_setup('日志管理')
        res1 = log.check_log_msg(project=task_name, msg='开始流量分析')
        res2 = log.check_log_msg(project=task_name, msg='停止流量分析')
        print res1, res2
        log.go_back()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res1 and res2)

    def test_C707386(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.auto_entry(scan_port=para.SCAN_PORT, ip_address=para.SCAN_SUBNET)
        asset.jump_to_threat(option='停止')
        log = project_navigation.goto_system_setup('日志管理')
        log.search_info(task_name)
        res1 = log.check_log_msg(project=task_name, msg='开始自动扫描')
        res2 = log.check_log_msg(project=task_name, msg='停止自动扫描')
        log.search_info(task_name+'A')
        res3 = log.check_log_msg(project=task_name, msg='开始自动扫描')
        res4 = log.check_log_msg(project=task_name, msg='停止自动扫描')
        print res1, res2, res3, res4
        log.go_back()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res1 and res2 and not res3 and not res4)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()         #关闭chrome浏览器'''

if __name__ == '__main__':
    unittest.main()