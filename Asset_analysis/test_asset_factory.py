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

    def test_C618947(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        result = asset.check_autocomplete()
        asset.discard_page()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C640425(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='施耐德（Schneider）',  model='Modicon M580', ip_address='')
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='西门子（Siemens）',  model='S7-1500', ip_address='')
        asset.add_device(device_type='集散控制系统（DCS）', vendor='艾默生（Emerson）',  model='DeltaV', ip_address='')
        asset.calculate_score()
        score1 = asset.get_score()
        asset.del_device_confirmation(device_name='Modicon M580')
        asset.calculate_score()
        score2 = asset.get_score()
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='西门子（Siemens）',  model='S7-300', ip_address='')
        asset.calculate_score()
        score3 = asset.get_score()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue((score2 not in score1) and (score3 not in score2))

    def test_C571727(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='施耐德（Schneider）',  model='Modicon M580', ip_address='')
        asset.calculate_score()
        asset.enter_vulner_detail()
        expectation = ['CVE','CNNVD', 'CNVD','漏洞公告','威胁类型','漏洞类型','漏洞结果','更新时间','发布时间','攻击复杂度','身份认证','可用性影响','机密性影响','完整性影响','攻击向量']
        result = None
        for info in expectation:
            if asset.check_vulner_detail(info):
                result = True
                print 'true '+info
            else:
                result = False
                print info
                break
        self.assertTrue(result)

    def test_C618913(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device()
        result = asset.check_autoscan_message()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C571722(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        asset = project_navigation.goto_asset_analysis()
        asset.add_plc()
        result = asset.vulnerability_detail()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    '''def test_C571740(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_multiarea_project(project_name=task_name, number_of_area=1, area_name=[task_name])
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry()
        asset.add_device()
        asset.go_back()
        asset.asset_entry_byname(task_name)
        asset.go_back()
        result = asset.del_asset_analysis(area_name=task_name)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)'''

    def tearDown(self):
        time.sleep(1)
        self.login.quit()  #关闭chrome浏览器
        time.sleep(3)

if __name__ =='__main__':
  unittest.main()