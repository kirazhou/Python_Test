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

    def test_C707252(self):
        task_name = str(int(time.time()))
        vendor_name = task_name
        model_type = task_name+'B'
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(vendor='Fox Software',  model='VFP', device_type ='数据服务器（DB）', ip_address='')
        asset.add_specific(vendor=vendor_name, model=model_type, device_type='数据服务器（DB）', ip_address='')
        asset.del_device_confirmation(vendor_name)
        asset.del_vendor(vendor_name, type='数据服务器（DB）')
        result = asset.check_vendor_selection(vendor_name)
        asset.discard_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertFalse(result)

    def test_C707303(self):
        task_name = str(int(time.time()))
        vendor_name = task_name
        model_type = task_name+'B'
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_specific(vendor=vendor_name, model=model_type, device_type='数据服务器（DB）', ip_address='')
        asset.del_device_confirmation(vendor_name)
        asset.del_vendor(vendor_name, type='数据服务器（DB）')
        result = asset.check_vendor_selection(vendor_name)
        asset.discard_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertFalse(result)

    def test_C707345(self):
        task_name = str(int(time.time()))
        vendor_name = task_name
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_specific(vendor=vendor_name, model='AA', device_type='数据服务器（DB）', ip_address='')
        result1 = asset.check_device_info(task_name)
        task_name2 = str(int(time.time()))
        asset.modify_vendor(vendor_name=task_name2, type='数据服务器（DB）', old_verdor=task_name)
        result2 = asset.check_device_info(task_name2)
        result3 = asset.check_device_info(task_name)
        print result1, result2, result3
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result1 and result2 and (not result3))

    """def test_C777606(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_multiarea_project(project_name=task_name, number_of_area=1, area_name=['123'])
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device_with_link(vendor='huawei(hw)', model='未知型号', device_type='加密认证设备（EAE）', ip_address='', ipaddress_1='0.0.0.0')
        res = asset.check_error_msg()
        self.assertTrue(res)"""

    def test_C777615(self):
        task_name = str(int(time.time()))
        vendor_name = task_name
        device_type = task_name+'B'
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_specific(vendor_name, device_type)
        asset.del_device_confirmation(vendor_name)
        asset.del_vendor(vendor_name)
        result = asset.check_vendor_selection(vendor_name)
        asset.discard_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertFalse(result)

    def test_C784151(self):
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

    def test_C784156(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_multiarea_project(project_name=task_name, number_of_area=1, area_name=['123'])
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device_without_area(vendor='匡恩（ACORN）', model='监测审计平台KEA-C200', device_type='入侵检测系统（IDS）', ip_address='')
        res = asset.check_button_disable()
        self.assertTrue(res)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()  #关闭chrome浏览器
        time.sleep(3)

if __name__ =='__main__':
  unittest.main()