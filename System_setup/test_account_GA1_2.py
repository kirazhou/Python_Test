# -*- coding:UTF-8 -*-
import unittest
import sys
import os
import time
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GemstoneLib.page_class import para, login_page

class Test_suite_traffic(unittest.TestCase):
    def setUp(self):
        self.login = login_page()
        self.project_manager = self.login.open_browser_to_login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)

    def test_C707469(self):
        acc_name = str(int(time.time()))
        acc = self.project_manager.goto_system_setup('账户管理')
        acc.create_new_account(user=acc_name, pwd='A12345678')
        acc.logout()
        self.login.login_page(acc_name, 'A12345678')
        acc.logout()
        self.login.login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)
        res = self.project_manager.check_welcome()
        self.project_manager.goto_system_setup('账户管理')
        acc.del_user(acc_name)
        self.assertTrue(res)

    def test_C707470(self):
        acc_name = str(int(time.time()))
        acc = self.project_manager.goto_system_setup('账户管理')
        acc.create_new_account(user=acc_name, pwd='A12345678')
        acc.edit_user(user=acc_name, new_pwd='B12345678')
        acc.logout()
        self.login.login_page(acc_name, 'B12345678')
        res = self.project_manager.check_welcome()
        acc.logout()
        self.login.login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)
        self.project_manager.goto_system_setup('账户管理')
        acc.del_user(acc_name)
        self.assertTrue(res)

    def test_C707473(self):
        acc_name = str(int(time.time()))
        acc = self.project_manager.goto_system_setup('账户管理')
        acc.create_new_account(user=acc_name, pwd='A12345678')
        acc.del_user(user=acc_name)
        acc.logout()
        self.login.open_browser_to_login_page(acc_name, 'A12345678')
        res = self.project_manager.check_welcome()
        self.assertFalse(res)

    def test_C707471(self):
        new_pwd = 'A12345678'
        acc = self.project_manager.goto_system_setup('账户管理')
        acc.reset_admin(oldpwd=para.ADMIN_USER_PASSWORD, newpwd=new_pwd)
        acc.logout()
        self.login.open_browser_to_login_page(para.ADMIN_USER, new_pwd)
        res = self.project_manager.check_welcome()
        acc = self.project_manager.goto_system_setup('账户管理')
        acc.reset_admin(oldpwd=new_pwd, newpwd=para.ADMIN_USER_PASSWORD)
        self.assertTrue(res)

    def test_C707472(self):
        info = str(int(time.time()))
        acc = self.project_manager.goto_system_setup('账户管理')
        infos1 = acc.get_company_infos()
        new_info = str(int(time.time()))
        acc.edit_company_info([info,info,'111111'])
        acc.yes()
        infos2 = acc.get_company_infos()
        acc.edit_company_info([new_info,new_info,'666666'])
        acc.no()
        infos3 = acc.get_company_infos()
        self.assertTrue(not(infos1 == infos2) and (infos2 == infos3))

    def test_C707490(self):
        pwd = 'A12345678'
        acc_name = str(int(time.time()))
        acc = self.project_manager.goto_system_setup('账户管理')
        acc.create_new_account(user=acc_name, pwd=pwd)
        acc.logout()
        self.login.login_page(acc_name, pwd)
        self.project_manager.goto_system_setup('用户信息')
        acc.edit_normal_user([acc_name, acc_name, acc_name, acc_name, acc_name+'@gmail.com'])
        res = acc.check_success_msg
        acc.logout()
        self.login.login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)
        self.project_manager.goto_system_setup('账户管理')
        acc.del_user(acc_name)
        self.assertTrue(res)

    def test_C707491(self):
        acc_name = str(int(time.time()))
        acc = self.project_manager.goto_system_setup('账户管理')
        acc.create_new_account(user=acc_name, pwd='A12345678')
        acc.logout()
        self.login.login_page(acc_name, 'A12345678')
        self.project_manager.goto_system_setup('用户信息')
        acc.reset_normal_pwd(oldpwd='A12345678', newpwd=para.ADMIN_USER_PASSWORD)
        acc.logout()
        self.login.login_page(acc_name, para.ADMIN_USER_PASSWORD)
        res = self.project_manager.check_welcome()
        acc.logout()
        self.login.login_page(para.ADMIN_USER, para.ADMIN_USER_PASSWORD)
        self.project_manager.goto_system_setup('账户管理')
        acc.del_user(acc_name)
        self.assertTrue(res)

    def tearDown(self):
        time.sleep(1)
        self.login.quit()          #关闭chrome浏览器
        time.sleep(3)

if __name__ =='__main__':
  unittest.main()