# -*- coding:UTF-8 -*-
import unittest
import sys
import os
import time
import datetime
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GemstoneLib.page_class import para, login_page


class Test_suite_threat_full(unittest.TestCase):
    def setUp(self):
        self.login = login_page()
        self.project_manager = self.login.open_browser_to_login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)

    def test_C578736(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form('电力监控系统')
        threat_analysis.fill_a_question()
        threat_analysis.go_back()
        project_navigation.goto_reports()
        threat = project_navigation.goto_threat_analysis()
        #check_form_status return 'blank' if there is no processing bar, return 'processing' if there is a processing bar
        result = threat.check_form_status('电力监控系统')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertEqual(result, 'processing')

    def test_C619025(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form('电力监控系统')
        threat_analysis.fill_a_question()
        threat_analysis.go_back()
        dtnow = datetime.datetime.now()
        dt = (str(dtnow))[:10]
        result = json.dumps(threat_analysis.check_update_time('电力监控系统'))
        print dt, result
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(dt in result)

    def test_C571702(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form('电力监控系统')
        threat_analysis.fill_a_question()
        threat_analysis.go_back()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)

    def test_C610560(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form(form_name='工业控制系统')
        threat_analysis.fill_questionnaire(1)
        threat_analysis.check_commit()
        first = json.dumps(threat_analysis.get_score())
        threat_analysis.close_report()
        threat_analysis.enter_form(form_name='工业控制系统', action='reset')
        threat_analysis.fill_a_question(answer='yes')
        threat_analysis.check_commit()
        second = json.dumps(threat_analysis.get_score())
        threat_analysis.close_report()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertNotEqual(second, first)

    def test_C571692(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form(form_name='工业控制系统')
        threat_analysis.fill_questionnaire(0)
        threat_analysis.check_commit()
        expectation1 = '100/100'
        expectation2 = 'SL4'
        result1 = json.dumps(threat_analysis.get_score())
        result2 = json.dumps(threat_analysis.get_level())
        threat_analysis.close_report()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue((expectation1 in result1) and (expectation2 in result2))

    def test_C571693(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form(form_name='工业控制系统')
        threat_analysis.fill_questionnaire(1)
        threat_analysis.check_commit()
        expectation1 = '0/100'
        expectation2 = json.dumps('不符')
        result1 = json.dumps(threat_analysis.get_score())
        result2 = json.dumps(threat_analysis.get_level())
        threat_analysis.close_report()
        threat_analysis.enter_form(form_name='工业控制系统', action='reset')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue((expectation1 in result1) and (expectation2 in result2))

    def test_C618037(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form(form_name='电力监控系统')
        threat_analysis.fill_questionnaire(1)
        threat_analysis.fill_question(index=1, choice='else', comment='this is a comment')
        threat_analysis.fill_question(index=1, choice='no')
        threat_analysis.fill_question(index=2, choice='else', comment='this is a comment')
        threat_analysis.fill_question(index=2, choice='no')
        threat_analysis.check_commit()
        result = json.dumps(threat_analysis.get_number_of_choice('否'))
        threat_analysis.close_report()
        threat_analysis.enter_form(form_name='电力监控系统', action='reset')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(('115' in result))

    def test_C619023(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        result1 = json.dumps(threat_analysis.check_description(form_name='工业控制'))
        expectation1 = json.dumps('本套威胁分析标准根据 GB/T 30976.1-2014 相关要求整理。')
        result2 = json.dumps(threat_analysis.check_name(form_name='工业控制'))
        expectation2 = json.dumps('工业控制系统信息安全评估规范')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue((expectation1 in result1) and (expectation2 in result2))

    def test_C640237(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form('电力监控系统')
        threat_analysis.fill_questionnaire(1)
        titles = ['安全管理制度', '安全管理机构', '人员安全管理', '系统建设管理', '系统运维管理']
        for title in titles:
            threat_analysis.select_sub_title(title=title)
            threat_analysis.fill_questions_in_current_page(answer='yes')
        threat_analysis.check_commit()
        first = json.dumps(threat_analysis.get_management_level()).strip('"')
        sec = json.dumps(threat_analysis.get_performance_level()).strip('"')
        score = json.dumps(threat_analysis.get_score()).strip('"')
        threat_analysis.close_report()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(first in json.dumps('达标') and sec in json.dumps('未达标') and int(score[:-4])<50)

    def test_C736410(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form('电力监控系统')
        threat_analysis.fill_questionnaire(0)
        threat_analysis.check_commit()
        score = json.dumps(threat_analysis.get_score()).strip('"')
        threat_analysis.close_report()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertEqual(int(score[:-4]), 100)

    def test_C736412(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form('电力监控系统')
        threat_analysis.fill_questions_in_current_page(answer='yes')
        threat_analysis.go_back()
        result1 = threat_analysis.check_form_status('电力监控系统')
        threat_analysis.reset_form(form_name='电力监控系统')
        result2 = threat_analysis.check_form_status('电力监控系统')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue((result1 is 'processing')and(result2 is 'blank'))

    def test_C736413(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form('电力监控系统')
        threat_analysis.fill_questionnaire(0)
        threat_analysis.go_back()
        threat_analysis.enter_form(form_name='电力监控系统', action='continue')
        result = threat_analysis.check_commit()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C736414(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form(form_name='电力监控系统')
        threat_analysis.fill_questionnaire(0)
        threat_analysis.check_commit()
        threat_analysis.close_report()
        result = threat_analysis.enter_form(form_name='电力监控系统', action='reset')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result)

    def test_C618943(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form('电力监控系统')
        threat_analysis.go_back()
        result = json.dumps(threat_analysis.enter_form('电力监控系统')).strip('"')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        print result
        self.assertTrue(len(result) > 0)

    def test_C571699(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form('电力监控系统')
        threat_analysis.fill_questions_in_current_page()
        threat_analysis.go_back()
        result = threat_analysis.check_form_status('电力监控系统')
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result is 'processing')

    def test_C571697(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        threat_analysis = project_navigation.goto_threat_analysis()
        threat_analysis.enter_form('电力监控系统')
        threat_analysis.fill_questions_in_current_page()
        threat_analysis.go_back()
        threat_analysis.sele_sort(key_word='正序排列')
        sort1 = threat_analysis.get_form_names()
        res1 = u'电力监控系统' in sort1[0]
        threat_analysis.sele_sort(key_word='从低到高')
        sort2 = threat_analysis.get_form_names()
        res2 = u'工业控制系统' in sort2[0]
        threat_analysis.sele_sort(key_word='从新到旧')
        sort2 = threat_analysis.get_form_names()
        res3 = u'电力监控系统' in sort2[0]
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        print res1, res2, res3
        self.assertTrue(res1 and res2 and res3)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()          #关闭chrome浏览器

if __name__ == '__main__':
    unittest.main()
