# -*- coding:UTF-8 -*-
import unittest
import sys
import os
import time
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GemstoneLib.page_class import para, login_page

class Test_suite_full(unittest.TestCase):
    def setUp(self):
        self.login = login_page()
        self.project_manager = self.login.open_browser_to_login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)

    def test_C571736(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='集散控制系统（DCS）', vendor='ABB',  model='AC800F',ip_address='')
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='施耐德（Schneider）',  model='Modicon M221 ',ip_address='')
        result_true = asset.check_device_info('AC800F')
        asset.search_device('Modicon M221')
        result_false = not asset.check_device_info('AC800F')
        asset.search_device('')
        result_true2 = asset.check_device_info('AC800F')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result_true and result_false and result_true2)

    def test_C571737(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='集散控制系统（DCS）', vendor='ABB',  model='AC800F', ip_address='')
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='施耐德（Schneider）',  model='Modicon M221 ', ip_address='')
        asset.calculate_score()
        asset.score_overview()
        result1 = asset.find_device_in_score_overview('集散控制系统（DCS）')
        asset.score_overview()
        result2 = asset.find_device_in_score_overview('可编程逻辑控制器（PLC）')
        asset.del_device_confirmation('PLC')
        asset.calculate_score()
        asset.score_overview()
        result3 = not asset.find_device_in_score_overview('可编程逻辑控制器（PLC）')
        asset.discard_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result1 and result2 and result3)

    def test_C736291(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_multiarea_project(project_name=task_name, number_of_area=1, area_name=[task_name+'B'])
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry(area=task_name+'B', method='手动录入资产')
        asset.add_device(device_type='集散控制系统（DCS）', vendor='ABB',  model='AC800F', ip_address='')
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='施耐德（Schneider）',  model='Modicon M221 ', ip_address='')
        asset.go_back()
        asset.asset_exist(area_name=task_name+'B')
        result = asset.get_area_name()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(task_name+'B' in result)

    def test_C581269(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='集散控制系统（DCS）', vendor='ABB',  model='AC800F',ip_address='')
        title_row = asset.check_title_row()
        result1 = json.dumps('IP地址') in title_row
        result2 = json.dumps('类型') in title_row
        result3 = json.dumps('厂商') in title_row
        result4 = json.dumps('型号') in title_row
        result5 = json.dumps('自设名称') in title_row
        result6 = json.dumps('输入方法') in title_row
        result7 = json.dumps('录入时间') in title_row
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result1 and result2 and result3 and result4 and result5 and result6 and result7)

    def test_C618004(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='集散控制系统（DCS）', vendor='ABB',  model='AC800F',ip_address='')
        result1 = asset.check_device_info('AC800F')
        asset.del_device_from_edit('AC800F')
        result2 = not asset.check_device_info('AC800F')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result1 and result2)

    def test_C595361(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='集散控制系统（DCS）', vendor='ABB',  model='AC800F',ip_address='')
        asset.go_back()
        asset.switch_sort_type('list')
        result = asset.asset_exist()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C618040(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='集散控制系统（DCS）', vendor='ABB',  model='AC800F',ip_address='')
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='施耐德（Schneider）',  model='Modicon M221 ',ip_address='')
        asset.calculate_score()
        asset.score_overview()
        asset.find_device_in_score_overview('集散控制系统（DCS）')
        asset.add_device(device_type='集散控制系统（DCS）', vendor='ABB',  model='AC800F',ip_address='')
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='施耐德（Schneider）',  model='Modicon M221 ',ip_address='')
        asset.calculate_score()
        asset.score_overview()
        asset.discard_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)

    def test_C618911(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='集散控制系统（DCS）', vendor='ABB',  model='AC800F',ip_address='')
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='施耐德（Schneider）',  model='Modicon M221 ',ip_address='')
        asset.calculate_score()
        asset.topology()
        asset.asets_topology_go_back()
        asset.asset_exist()
        result = asset.check_device_info(key_info='AC800F')
        result2 = asset.check_device_info(key_info='Modicon M221 ')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result and result2)

    def test_C618962(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.auto_entry(scan_port=para.SCAN_PORT, ip_address=para.SCAN_SUBNET)
        asset.asets_topology_go_back()
        result1 = asset.asset_exist()
        asset.del_device_confirmation()
        asset.go_back()
        result2 = asset.asset_exist()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result1 and not result2)

    def test_C622927(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='集散控制系统（DCS）', vendor='ABB',  model='AC800F', ip_address='')
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='施耐德（Schneider）',  model='Modicon M221 ', ip_address='')
        asset.go_back()
        result = asset.asset_exist()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C736268(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='集散控制系统（DCS）', vendor='ABB',  model='AC800F', ip_address='')
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='施耐德（Schneider）',  model='Modicon M221 ', ip_address='')
        result1 = asset.check_device_info(key_info='AC800F')
        asset.del_device_confirmation(device_name='AC800F')
        asset.search_device(device_name='')
        result2 = not asset.check_device_info(key_info='AC800F')
        result3 = asset.check_device_info(key_info='Modicon M221 ')
        print result1, result2, result3
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result1 and result2 and result3)

    def test_C617738(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='西门子（Siemens）',  model='S7-1200',ip_address='')
        asset.calculate_score()
        asset.enter_vulner_detail()
        result = asset.check_vulner_detail(key_info='威胁类型')
        self.assertTrue(result)

    def test_C618006(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='西门子（Siemens）',  model='S7-1200',ip_address='')
        asset.try_to_del()
        result = asset.check_device_info(key_info='S7-1200')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C639820(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_multiarea_project(project_name=task_name, number_of_area=1, area_name=['A'])
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry(area='A')
        asset.add_device(device_type=' 网闸（Gap）', vendor='安盟华御（Anmit）',  model='SU-GAP',ip_address='', link=True)
        # asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='西门子（Siemens）',  model='S7-1200',ip_address='')
        asset.go_back()
        b_exist = asset.asset_exist(area_name='默认区域名称')
        asset.go_back()
        asset.asset_exist(area_name='A')
        asset.del_device_from_edit(device_name='SU-GAP')
        asset.go_back()
        time.sleep(1)
        b_not_exist = asset.asset_exist(area_name='默认区域名称')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(b_exist and not b_not_exist)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()  #关闭chrome浏览器
        time.sleep(3)

if __name__ =='__main__':
  unittest.main()