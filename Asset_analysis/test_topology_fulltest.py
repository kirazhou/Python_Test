# -*- coding:UTF-8 -*-
import unittest
import sys
import os
import json
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GemstoneLib.page_class import para, login_page

class Test_suite_1(unittest.TestCase):
    def setUp(self):
        self.login = login_page()
        self.project_manager = self.login.open_browser_to_login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)

    def test_C618050(self):
        task_name = str(int(time.time()))
        d_type = 'OPC服务器（OPC）'
        d_vendor = 'Matrikon'
        d_model = 'OPCClient'
        invaild_ip = para.TEST_SERVER_IP+'/24'
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        check1 = asset.auto_entry(scan_port=para.SCAN_PORT, ip_address=invaild_ip)
        asset.manul_entry()
        asset.add_device(device_type=d_type, vendor=d_vendor, model=d_model)
        check_type = asset.check_device_info(d_type)
        check_vendor = asset.check_device_info(d_vendor)
        check_model = asset.check_device_info(d_model)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(check_type and check_vendor and check_model and not check1)

    def test_C618912(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.auto_entry(scan_port=para.SCAN_PORT, ip_address=para.SCAN_SUBNET)
        subnet = asset.get_subnet_in_topology()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(para.SCAN_SUBNET in subnet)

    def test_C618915(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(vendor='未知厂商',  model='未知型号', device_type='未知类型', ip_address='')
        asset.add_device(vendor='Matrikon',  model='OPCClient', device_type='OPC服务器（OPC）', ip_address='3.3.3.3')
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='Triangle', model='Nano-10', ip_address='6.6.6.6')
        # asset.add_device(vendor='Fox Software',  model='VFP', device_type='数据服务器（DB）', ip_address='9.8.7.6')
        # asset.auto_entry(ip_address=para.SCAN_SUBNET)
        # time.sleep(150)
        # asset.go_back()
        # asset.asset_exist()
        dev_info_list = asset.check_all_device_version()
        undefined = json.dumps('未知').strip('"')
        counter = 0
        for dev in dev_info_list:
            if (undefined not in json.dumps(dev[0])) and (undefined not in json.dumps(dev[2])) and (len(dev[4]) > 0):
                counter += 1
        asset.calculate_score()
        asset.topology()
        number = json.dumps(asset.get_number_of_device_with_compeleted_info()[:-1].strip())
        exp, result = json.dumps(counter), number.strip('"')
        self.assertEqual(exp, result)

    """def test_C588247(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        # asset.manul_entry()
        # asset.add_device(vendor='Matrikon',  model='OPCClient', device_type='OPC服务器（OPC）', ip_address='3.3.3.3')
        # asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='Triangle', model='Nano-10', ip_address='6.6.6.6')
        # asset.calculate_score()
        # asset.topology()
        asset.auto_entry(scan_port=para.SCAN_PORT, ip_address=para.SCAN_SUBNET)
        score = asset.get_score_in_topology()[:-5]
        self.assertEqual(float(score), int(score))"""

    def test_C571725(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(vendor='西门子（Siemens）',  model='S7-1200', device_type='可编程逻辑控制器（PLC）', ip_address='')
        asset.calculate_score()
        asset.enter_vulner_detail()
        res = True
        details = json.dumps(asset.get_device_detail())
        expectation = json.dumps([u'西门子（Siemens）', u'S7-1200', u'可编程逻辑控制器（PLC）', u'设备名称', u'设备厂商', u'设备固件版本号', u'设备描述', u'设备型号'])
        for i in expectation:
            if i not in details:
                res = False
        asset.close_vulner_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()  #关闭chrome浏览器
        time.sleep(3)

if __name__ =='__main__':
  unittest.main()