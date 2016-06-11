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

    def test_C603385(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='交换机（Switch）', vendor='思科（Cisco）', model='CSS 11000', ip_address='')
        asset.calculate_score()
        asset.score_overview()
        result = asset.find_device_in_top5_threat('思科（Cisco）')
        asset.discard_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C618003(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='交换机（Switch）', vendor='思科（Cisco）', model='CSS 11000', ip_address='9.9.9.9')
        asset.calculate_score()
        asset.score_overview()
        result_vendor = asset.find_device_in_top5_threat('思科（Cisco）')
        result_model = asset.find_device_in_top5_threat('CSS 11000')
        result_ip = asset.find_device_in_top5_threat('9.9.9.9')
        asset.discard_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result_ip and result_model and result_vendor)

    def test_C602492(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        for i in range(3):
            asset.add_device(device_type='数据服务器（DB）', vendor='亚控（Wellintech）', model='KingHistorian', ip_address='')
        asset.calculate_score()
        asset.score_overview()
        result = asset.count_vulnerability_in_top5_threat()
        asset.discard_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertEqual(result, 1)

    def test_C640906(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='数据服务器（DB）', vendor='亚控（Wellintech）', model='KingHistorian', ip_address='')
        asset.calculate_score()
        asset.score_overview()
        result = asset.find_vulnerability_CVE()
        asset.discard_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C590626(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.auto_entry(scan_port=para.SCAN_PORT, ip_address=para.SCAN_SUBNET)
        asset.asets_topology_go_back()
        asset.asset_exist()
        asset.add_device(device_type='集散控制系统（DCS）', vendor='艾默生（Emerson）', model='DeltaV', ip_address='')
        step1 = asset.check_device_info(key_info='DeltaV')
        asset.calculate_score()
        asset.score_overview()
        step2 = True
        infos = ['区域设备数', '信息齐全设备','全网漏洞','网段设备显示','高威胁评分设备 前五名','最危险漏洞 前五名']
        for info in infos:
            print info
            if asset.check_info_in_score_overview(key_info=info):
                pass
            else:
                step2 = False
                break
        asset.discard_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(step1 and step2)

    def test_C618948(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.auto_entry(scan_port=para.SCAN_PORT, ip_address=para.SCAN_SUBNET)
        score1 = asset.get_score_in_topology()
        asset.asets_topology_go_back()
        asset.asset_exist()
        # asset.manul_entry()
        # asset.add_device(device_type='集散控制系统（DCS）', vendor='艾默生（Emerson）', model='DeltaV', ip_address='')
        asset.modify_device(vendor='西门子（Siemens）', device_model='S7-1200', device_type='可编程逻辑控制器（PLC）', index=1)
        asset.calculate_score()
        score2 = asset.get_score()
        asset.enter_vulner_detail()
        result = asset.check_vulner_detail(key_info='CVE')
        result2 = score1[:-5] is not score2[:-4]
        self.assertTrue(result and result2)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()  #关闭chrome浏览器
        time.sleep(3)

if __name__ =='__main__':
  unittest.main()