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

    def test_C618963(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.auto_entry(scan_port=para.SCAN_PORT, ip_address=para.SCAN_SUBNET)
        result = asset.find_ip_in_topology(para.TEST_SERVER_IP)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertFalse(result)

    def test_C618919(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.auto_entry(scan_port=para.SCAN_PORT, ip_address='192.111.15.125/24')
        result = asset.get_number_of_devices_in_topology()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertEqual(result, '0')

    def test_C571743(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.auto_entry(scan_port=para.SCAN_PORT, ip_address=para.SCAN_SUBNET)
        asset.asets_topology_go_back()
        asset.manul_entry()
        asset.add_device(vendor='Fox Software',  model='VFP', device_type='数据服务器（DB）', ip_address='9.8.7.6')
        result = asset.check_device_info('9.8.7.6')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C736391(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.auto_entry(scan_port=para.SCAN_PORT, ip_address=para.SCAN_SUBNET)
        asset.jump_to_threat(option='停止')
        result = asset.get_current_page(title='威胁分析')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    """def test_C736392(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.auto_entry(scan_port=para.SCAN_PORT, ip_address=para.SCAN_SUBNET)
        time.sleep(30)
        asset.jump_to_threat(option='停止并保存')
        project_navigation.goto_asset_analysis()
        result = asset.asset_exist()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)"""

    def test_C578735(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        result = asset.cancel_autoscan(scan_port=para.SCAN_PORT, subnet_ip=para.SCAN_SUBNET)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C571730(self):
        task_name = str(int(time.time()))
        names =['A', 'B', 'C']
        project_navigation = self.project_manager.build_multiarea_project(project_name=task_name, number_of_area=3, area_name=names)
        asset = project_navigation.goto_asset_analysis()
        name_list = asset.get_area_name_from_dropdown()
        result = True
        for i in range(len(name_list)):
            if names[i] not in name_list[i]:
                result = False
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    """def test_C602357(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(vendor='Matrikon',  model='OPCClient', device_type='OPC服务器（OPC）', ip_address='192.168.0.112')
        asset.search_device('192.168.0.112')
        result = asset.check_device_info('Matrikon')
        asset.go_back()
        asset.auto_entry(scan_port=para.SCAN_PORT, ip_address=para.SCAN_SUBNET)
        time.sleep(15)
        asset.go_back()
        asset.asset_exist()
        asset.search_device('192.168.0.112')
        cannot_find = not asset.check_device_info('Matrikon')
        find = asset.check_device_info('CASWELL')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result and cannot_find and find)"""

    def test_C683444(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.auto_entry(scan_port=para.SCAN_PORT, ip_address=para.SCAN_SUBNET)
        result = asset.find_ip_in_topology(para.TEST_SERVER_IP)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertFalse(result)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()  #关闭chrome浏览器
        time.sleep(3)

if __name__ =='__main__':
  unittest.main()