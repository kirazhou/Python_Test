# -*- coding:UTF-8 -*-
import unittest
import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GemstoneLib.page_class import para, login_page

class Test_suite_1(unittest.TestCase):
    def setUp(self):
        self.login = login_page()
        self.project_manager = self.login.open_browser_to_login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)

    def test_C581268(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        Asset_analysis = project_navigation.goto_asset_analysis()
        Asset_analysis.begin()
        res = Asset_analysis.cancellation_of_assetentry()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res)

    def test_C588245(self):
        # TODO: not inculde all illegal cases
        task_name = str(int(time.time()))
        invaild_ip = '0.0.0.0/32'
        project_navigation = self.project_manager.build_project(task_name)
        Asset_analysis = project_navigation.goto_asset_analysis()
        result = Asset_analysis.asset_autoscan(invaild_ip)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C736973(self):
        # TODO: not inculde all illegal cases
        task_name = str(int(time.time()))
        invaild_ip = '0.0.0.0/32'
        project_navigation = self.project_manager.build_project(task_name)
        Asset_analysis = project_navigation.goto_asset_analysis()
        result = Asset_analysis.asset_autoscan(invaild_ip)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C618005(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        Asset_analysis = project_navigation.goto_asset_analysis()
        Asset_analysis.manul_entry()
        Asset_analysis.add_device()
        result = Asset_analysis.del_device_confirmation()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C581263(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        Asset_analysis = project_navigation.goto_asset_analysis()
        first = Asset_analysis.stop_autoscan(scan_port=para.SCAN_PORT, subnet_ip=para.SCAN_SUBNET)
        second = Asset_analysis.stop_save_autoscan(scan_port=para.SCAN_PORT, subnet_ip=para.SCAN_SUBNET)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(first and second)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()  #关闭chrome浏览器
        time.sleep(3)

if __name__ =='__main__':
  unittest.main()