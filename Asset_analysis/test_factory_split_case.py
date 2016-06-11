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

    def test_C707249(self):
        task_name = str(int(time.time()))
        d_type = 'OPC服务器（OPC）'
        d_vendor = 'Matrikon'
        d_model = 'OPCClient'
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.add_plc()
        asset.modify_device(device_type=d_type, vendor=d_vendor, device_model=d_model)
        check_type = asset.check_device_info(d_type)
        check_vendor = asset.check_device_info(d_vendor)
        check_model = asset.check_device_info(d_model)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(check_type and check_vendor and check_model)

    def test_C707247(self):
        task_name = str(int(time.time()))
        d_type = '可编程逻辑控制器（PLC）'
        d_vendor = 'Triangle'
        d_model = 'Nano-10'
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.add_plc()
        asset.modify_device(device_type=d_type, vendor=d_vendor, device_model=d_model)
        check_model = asset.check_device_info(d_model)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(check_model)

    def test_C707244(self):
        task_name = str(int(time.time()))
        d_type = '可编程逻辑控制器（PLC）'
        d_vendor = task_name
        d_model = task_name
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_specific(device_type=d_type, vendor=d_vendor, model=d_model)
        check_type = asset.check_device_info(d_type)
        check_vendor = asset.check_device_info(d_vendor)
        check_model = asset.check_device_info(d_model)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(check_type and check_vendor and check_model)

    def test_C707246(self):
        task_name = str(int(time.time()))
        d_type = '可编程逻辑控制器（PLC）'
        d_vendor = task_name
        d_model = task_name+'B'
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_specific(device_type=d_type, vendor=d_vendor, model=d_model)
        asset.del_device_confirmation(d_model)
        asset.add_device(device_type=d_type, vendor=d_vendor, model=d_model)
        check_type = asset.check_device_info(d_type)
        check_vendor = asset.check_device_info(d_vendor)
        check_model = asset.check_device_info(d_model)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(check_type and check_vendor and check_model)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()  #关闭chrome浏览器
        time.sleep(3)

if __name__ =='__main__':
  unittest.main()