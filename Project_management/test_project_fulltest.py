# -*- coding:UTF-8 -*-
import unittest
import sys
import os
import time
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GemstoneLib.page_class import para, login_page


class Test_suite_project(unittest.TestCase):
    def setUp(self):
        self.login = login_page()
        self.project_manager = self.login.open_browser_to_login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)

    def test_C571747(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_multiarea_project(project_name=task_name, number_of_area=1, area_name=['test'])
        basic = project_navigation.goto_basic_info()
        basic.edit_project()
        name1 = basic.get_area_name(1)
        basic.del_area(1)
        basic.save_change()
        name2 = basic.get_area_name(1)
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue('test' in json.dumps(name1) and not name2)

    def test_C571748(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        project_navigation.goto_project_manager()
        pn = self.project_manager.build_project(task_name+'B')
        basic = pn.goto_basic_info()
        basic.edit_project()
        basic.rename_project(new_name=task_name)
        basic.save_change()
        msg = basic.project_name_alert()
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(task_name in json.dumps(msg))

    def test_C571749(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        basic = project_navigation.goto_basic_info()
        new_infos = [u'projectname', u'company', u'address', u'123456', u'contacts', u'department', u'456']
        basic.edit_project()
        basic.change_infos(new_infos)
        basic.cancel_change()
        first = basic.get_info()
        basic.edit_project()
        basic.change_infos(new_infos)
        basic.save_change()
        second = basic.get_info()
        result1 = True
        result2 = True
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(u'projectname')
        for i in range(len(first)):
            if first[i] in new_infos[i]:
                result1 = False
        for i in range(len(second)):
            if second[i] not in new_infos[i]:
                result2 = False
        self.assertTrue(result1 and result2)

    def test_C602355(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_multiarea_project(project_name=task_name, number_of_area=1, area_name=['test'])
        asset = project_navigation.goto_asset_analysis()
        asset.manul_entry(area='test')
        asset.add_device(device_type='可编程逻辑控制器（PLC）', vendor='施耐德（Schneider）',  model='Modicon M580', ip_address='')
        basic = project_navigation.goto_basic_info()
        basic.edit_project()
        basic.add_area('test')
        basic.save_change()
        msg1 = basic.get_alert()
        print msg1
        result1 = u'区域名称不能重复' in msg1
        basic.cancel_change()
        basic.edit_project()
        basic.del_area(1)
        msg2 = basic.get_alert()
        basic.cancel_change()
        print msg2
        result2 = u'此区域已产生分析数据无法删除' in msg2
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result1 and result2)

    def test_C618033(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_multiarea_project(project_name=task_name, number_of_area=1, area_name=['test'])
        basic = project_navigation.goto_basic_info()
        basic.edit_project()
        basic.rename_project('new_name')
        msg = basic.check_cancel_pop_window()
        expec = json.dumps('当前项目信息还没有保存，确定要放弃编辑吗').strip('"')
        self.assertTrue(expec in expec)

    def test_C640411(self):
        task_name = str(int(time.time()))
        project_navigation = self.project_manager.build_project(task_name)
        project_navigation.goto_project_manager()
        self.project_manager.edit_project()
        self.project_manager.select_project()
        result1 = self.project_manager.del_button()
        self.project_manager.clear_selection()
        result2 = self.project_manager.del_button()
        self.project_manager.cancel_edit()
        self.project_manager.delete_project(task_name)
        self.assertTrue(result1 and not result2)

    def test_C578734(self):
        task_name = str(int(time.time()))
        self.project_manager.cancel_build_project(task_name)
        self.project_manager.cancel_build()
        self.project_manager.back_to_build()
        title1 = self.project_manager.get_current_page()
        self.project_manager.cancel_build()
        self.project_manager.exit_build()
        title2 = self.project_manager.get_current_page()
        print title1, title2, type(title1), type(title2)
        page1 = u'项目基本信息'
        page2 = u'项目管理'
        self.assertTrue(page1 in title1 and page2 in title2)

    def test_C618986(self):
        test1 = [u'项123Aa-_+',u'项123Aa-_+',u'项123Aa-_+',u'123456',u'项123Aa-_+',u'项123Aa-_+',u'123456-_+']
        test2 = [u'项123Aa-_+*',u'项123Aa-_+^',u'项123Aa-_+',u'123456',u'项123Aa-_+',u'项123Aa-_+',u'123456-_+']
        self.project_manager.start_project()
        self.project_manager.input_project(test1)
        result1 = self.project_manager.save_disable()
        self.project_manager.input_project(test2)
        result2 = self.project_manager.save_disable()
        self.assertTrue(not result1 and result2)

    def test_C707344(self):
        task_name = str(int(time.time()))
        self.project_manager.build_multiarea_project(project_name=task_name, number_of_area=1, area_name=['test'])
        self.project_manager.goto_project_manager()
        self.project_manager.delete_project(task_name)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()          #关闭chrome浏览器

if __name__ =='__main__':
  unittest.main()