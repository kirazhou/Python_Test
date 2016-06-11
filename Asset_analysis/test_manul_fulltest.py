# -*- coding:UTF-8 -*-
import unittest
import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GemstoneLib.page_class import para, login_page

class Test_suite_full(unittest.TestCase):
    def setUp(self):
        self.login = login_page()
        self.project_manager = self.login.open_browser_to_login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)

    def test_C618008(self):
        task_name = str(int(time.time()))
        vendor_name = task_name
        device_type = task_name+'B'
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_specific(vendor_name, device_type)
        result = asset.check_vendor_selection(vendor_name)
        asset.discard_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C618946(self):
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

    def test_C571733(self):
        task_name = str(int(time.time()))
        vendor_name = task_name
        device_type = task_name+'B'
        ip_addtess = '192.168.123.123'
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_specific(vendor_name, device_type, ip_addtess)
        result = asset.ip_conflict_message(vendor_name, device_type, ip_addtess)
        asset.discard_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C602495(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device()
        asset.go_back()
        asset.del_asset_analysis()
        asset.manul_entry()
        asset.add_device()
        asset.go_back()
        result = asset.asset_exist()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C639821(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        result = asset.cancel_add_device()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C639822(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(vendor='三菱（Mitsubishi）',  model='MX OPC Server', device_type ='OPC服务器（OPC）', ip_address='')
        asset.add_device(vendor='ABB',  model='Control Builder', device_type ='工程师站（EWS）', ip_address='')
        result1 = asset.check_device_info('Mitsubishi')
        result2 = asset.check_device_info('ABB')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue((result1 and result2))

    def test_C640408(self):
        task_name = str(int(time.time()))
        vendor = task_name
        model = task_name
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_specific(vendor=vendor, model=model)
        result = asset.duplicate_device_entry(vendor=vendor)
        time.sleep(3)
        asset.discard_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C595323(self):
        task_name = str(int(time.time()))
        d_vendor = task_name
        d_model = task_name
        another_vendor = d_vendor+'B'
        another_model = d_model+'B'
        new_vendor = 'Matrikon'
        new_model = 'OPCClient'
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_specific(vendor=d_vendor, model=d_model)
        asset.add_specific(vendor=another_vendor, model=another_model)
        asset.modify_device(vendor=new_vendor, device_model=new_model, device_type='OPC服务器（OPC）')
        result1 = asset.check_device_info(new_model)
        result2 = asset.check_device_info(new_vendor)
        self.assertTrue((result1 and result2))
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)

    def test_C618945(self):
        task_name = str(int(time.time()))
        d_vendor = task_name
        d_model = task_name+'A'
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_specific(vendor=d_vendor, model=d_model)
        asset.calculate_score()
        asset.topology()
        result = asset.find_device_in_topology(d_model)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C683446(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='Triangle', model='Nano-10', ip_address='')
        asset.add_device(device_type='OPC服务器（OPC）', vendor='Matrikon', model='OPCClient', ip_address='')
        asset.calculate_score()
        asset.go_back()
        asset.asset_exist()
        score_exist = asset.get_score()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(score_exist)

    def test_C683445(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        result = asset.check_undifined(device_type='可编程逻辑控制器（PLC）', vendor='西门子（Siemens）')
        asset.discard_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    '''def test_C602491(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.auto_entry(scan_port=para.SCAN_PORT, ip_address=para.SCAN_SUBNET)
        asset.go_back()
        asset.asset_exist()
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='Triangle', model='Nano-10', ip_address='2.2.2.2')
        result = asset.check_device_info('2.2.2.2')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)'''

    def tearDown(self):
        time.sleep(1)
        self.login.quit()  #关闭chrome浏览器
        time.sleep(3)

if __name__ =='__main__':
  unittest.main()