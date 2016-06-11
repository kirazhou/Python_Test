# -*- coding:UTF-8 -*-
import unittest
import sys
import os
import time
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GemstoneLib.page_class import para, login_page

class Test_suite_adds_functionality(unittest.TestCase):
    def setUp(self):
        self.login = login_page()
        self.project_manager = self.login.open_browser_to_login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)
    # def test_fill_questionnaire(self):
    #     task_name = str(int(time.time()))
    #     project_navigation = self.project_manager.build_project(task_name)
    #     # project_navigation = self.project_manager.goto_project('1')
    #     Threat_analysis = project_navigation.goto_threat_analysis()
    #     Threat_analysis.begin()
    #     Threat_analysis.fill_questionnaire(1)

    def test_C618009(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        result = json.dumps(threat_analysis.enter_form('工业控制系统信息安全评估规范'))
        expectation = json.dumps("本套威胁分析标准根据 GB/T 30976.1-2014 工业控制系统信息安全评估规范的相关要求整理，适用于系统设计方、设备生产商、系统集成商、工程公司、用户、资产所有人以及评估认证机构等对工业控制系统的信息安全进行评估时使用。")
        self.assertEqual(result, expectation)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)

    def test_C571705(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form('工业控制系统信息安全评估规范')
        result = json.dumps(threat_analysis.goto_subtitle())
        expectation = json.dumps("信息安全组织机构")
        self.assertEqual(result, expectation)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)

    def test_C571703(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form('工业控制系统信息安全评估规范')
        self.assertTrue(threat_analysis.fill_and_reset())
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)

    def test_C571704(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.begin()
        first = threat_analysis.check_commit()
        threat_analysis.close_report()
        threat_analysis.fill_questionnaire(1)
        second = threat_analysis.check_commit()
        threat_analysis.close_report()
        self.assertTrue(second and not first)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)

    def test_C640888(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form('电力监控系统')
        result = threat_analysis.fill_and_change_level()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)


    def tearDown(self):
        time.sleep(1)
        self.login.quit()          #关闭chrome浏览器

if __name__ =='__main__':
  unittest.main()
