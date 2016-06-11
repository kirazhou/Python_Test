# -*- coding:UTF-8 -*-
import unittest
import sys
import os
import time
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GemstoneLib.page_class import para, login_page

class Test_suite_report1_2(unittest.TestCase):
    def setUp(self):
        self.login = login_page()
        self.project_manager = self.login.open_browser_to_login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)

    def test_C736430(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        report = project_navigation.goto_reports()
        report.edit_info('测评实施对象信息')
        res = report.get_infos()
        report.cancel_change()
        report.edit_info('测评实施对象信息')
        report.re_enter_infos(['2', '2', '222222', '2', '2', '2'])
        report.cancel_change()
        report.edit_info('测评实施对象信息')
        res1 = report.get_infos()
        report.re_enter_infos(['3', '3', '333333', '3', '3', '3'])
        report.confirm_change()
        report.edit_info('测评实施对象信息')
        res2 = report.get_infos()
        report.cancel_change()
        print res, res1, res2
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res == res1 and [u'3', u'3', u'333333', u'3', u'3', u'3'] ==res2)

    def test_C736431(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        report = project_navigation.goto_reports()
        report.edit_info('测评实施人员信息')
        res = report.get_infos()
        report.cancel_change()
        report.edit_info('测评实施人员信息')
        report.re_enter_infos(['2', '2', '222222', '2qwe@gmail.com'])
        report.cancel_change()
        report.edit_info('测评实施人员信息')
        res1 = report.get_infos()
        report.re_enter_infos(['3', '3', '333333', '3qwe@gmail.com'])
        report.confirm_change()
        report.edit_info('测评实施人员信息')
        res2 = report.get_infos()
        report.cancel_change()
        print res, res1, res2
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res == res1 and [u'3', u'3', u'333333', u'3qwe@gmail.com'] ==res2)

    def test_C736432(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        report = project_navigation.goto_reports()
        report.edit_info('测评实施单位信息')
        res = report.get_infos()
        report.cancel_change()
        report.edit_info('测评实施单位信息')
        report.re_enter_infos(['2', '2', '222222'])
        report.cancel_change()
        report.edit_info('测评实施单位信息')
        res1 = report.get_infos()
        report.re_enter_infos(['3', '3', '333333'])
        report.confirm_change()
        report.edit_info('测评实施单位信息')
        res2 = report.get_infos()
        report.cancel_change()
        print res, res1, res2
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res == res1 and [u'3', u'3', u'333333'] ==res2)

    def test_C736847(self):
        acc_name = str(int(time.time()))
        acc = self.project_manager.goto_system_setup('账户管理')
        acc.create_new_account(user=acc_name, pwd='A12345678')
        acc.logout()
        self.login.open_browser_to_login_page(acc_name, 'A12345678')
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        report = project_navigation.goto_reports()
        report.edit_info('测评实施人员信息')
        res = report.get_infos()
        report.cancel_change()
        report.edit_info('测评实施人员信息')
        report.re_enter_infos(['2','2', '2', '222222', '2qwe@gmail.com'])
        report.cancel_change()
        report.edit_info('测评实施人员信息')
        res1 = report.get_infos()
        report.re_enter_infos(['3', '3', '3', '333333', '3qwe@gmail.com'])
        report.confirm_change()
        report.edit_info('测评实施人员信息')
        res2 = report.get_infos()
        report.cancel_change()
        print res, res1, res2
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res == res1 and res2 != res1)

    def test_C747388(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form(form_name='电力监控系统')
        threat_analysis.fill_questionnaire(0)
        threat_analysis.check_commit()
        threat_analysis.close_report()
        report = project_navigation.goto_reports()
        time.sleep(2)
        res = report.check_threat_report(name='电力监控系统安全防护评估规范')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res)

    def test_C747390(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        traffic_analysis = project_navigation.goto_traffic_analysis()
        traffic_analysis.start_analysis()
        traffic_analysis.start_setting()
        traffic_analysis.set_parameter(min='1', size='1')
        traffic_analysis.start_intercept()
        time.sleep(75)
        traffic_analysis.go_back()
        report = project_navigation.goto_reports()
        time.sleep(2)
        res = report.check_traffic_report(area_name='默认区域名称')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res)

    def test_C747403(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        report = project_navigation.goto_reports()
        report.edit_info('测评实施人员信息')
        res = report.get_infos()
        report.cancel_change()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res[0] is not None)

    def test_C747408(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        report = project_navigation.goto_reports()
        report.edit_info('测评实施单位信息')
        res = report.get_infos()
        report.cancel_change()
        report.edit_info('测评实施单位信息')
        report.re_enter_infos(['2', '2', '222222'])
        report.cancel_change()
        report.edit_info('测评实施单位信息')
        res1 = report.get_infos()
        report.re_enter_infos(['3', '3', '333333'])
        report.confirm_change()
        report.edit_info('测评实施单位信息')
        res2 = report.get_infos()
        report.cancel_change()
        print res, res1, res2
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(res == res1 and [u'3', u'3', u'333333'] ==res2)


    def tearDown(self):
        time.sleep(1)
        self.login.quit()          #关闭chrome浏览器
        time.sleep(3)

if __name__ =='__main__':
  unittest.main()