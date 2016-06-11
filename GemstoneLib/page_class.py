# -*- coding:UTF-8 -*-
from selenium import webdriver
import time
import json
from selenium.webdriver.common.action_chains import ActionChains


# 参数类
# '192.168.20.241'
class _para:
    def __init__(self):
        self.ADMIN_USER = 'admin'
        # self.ADMIN_USER_PASSWORD = 'admins'
        self.ADMIN_USER_PASSWORD = 'admin@12345'
        self.TEST_SERVER_IP = '172.18.54.33'
        self.SCAN_SUBNET = '192.168.1.125/24'
        self.SCAN_PORT = '192.168.1.185'

para = _para()

# 登录界面类
class login_page:
    def __init__(self):
        self.driver = webdriver.Chrome()

    # 打开浏览器进入登录界面
    def open_browser_to_login_page(self, user, pwd):
        driver = self.driver
        driver.get("https://" + para.TEST_SERVER_IP)
        driver.maximize_window()
        for i in range(1, 120):
            try:
                driver.find_element_by_id("inputUsername").clear()
            except:
                time.sleep(1)
        try:
            driver.find_element_by_id("inputUsername").send_keys(user)
        except:
            print u'网络连接有问题，请检查网络'
            return False
        driver.find_element_by_id("inputPassword").clear()
        driver.find_element_by_id("inputPassword").send_keys(pwd)
        driver.find_element_by_xpath("//button[contains(@class, 'center btn btn-primary')]").click()
        return project_manager(driver=self.driver)

    def login_page(self, user, pwd):
        driver = self.driver
        driver.find_element_by_id("inputUsername").clear()
        driver.find_element_by_id("inputUsername").send_keys(user)
        driver.find_element_by_id("inputPassword").clear()
        driver.find_element_by_id("inputPassword").send_keys(pwd)
        driver.find_element_by_xpath("//button[contains(@class, 'center btn btn-primary')]").click()
        return project_manager(driver=self.driver)

    def quit(self):
        driver = self.driver    # 关闭浏览器
   #     driver.quit()

    def wait_until_clickable(self, xpath):
        for i in range(0, 30):
            try:
                self.driver.find_element_by_xpath(xpath).click()
                break
            except:
                time.sleep(0.5)

    # 检测到元素存在
    def wait_until_visible(self, xpath):
        for i in range(0, 30):
            try:
                self.driver.find_element_by_xpath(xpath)
                break
            except:
                time.sleep(0.5)

# login_page = _login_page()


class project_manager:
    def __init__(self, driver):
        self.driver = driver
    # def goto_project(self, project_name):
    #     self.wait_until_clickable("//span[text()='%s']" % project_name)
    #     print ("//span[text()='%s']" % project_name)
    #     return project_navigation(driver=self.driver)

    def check_welcome(self):
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//span[@class='section-title' and text()='项目管理']")
            return True
        except:
            return False

    def goto_system_setup(self, selection):
        time.sleep(2)
        self.wait_until_clickable("//div[@class='logout']")
        time.sleep(2)
        # options = ['账户管理','系统设置','无线设置','版本信息','系统升级']
        self.wait_until_clickable("//a[text()='%s']" % selection)
        time.sleep(2)
        return System_setup(driver=self.driver)

    def goto_system(self, user, pwd):
        driver = self.driver
        driver.find_element_by_id("inputUsername").clear()
        driver.find_element_by_id("inputUsername").send_keys(user)
        driver.find_element_by_id("inputPassword").clear()
        driver.find_element_by_id("inputPassword").send_keys(pwd)
        driver.find_element_by_xpath("//button[contains(@class, 'center btn btn-primary')]").click()

    def goto_project_manager(self):
        self.wait_until_clickable("//span[text()='项目管理']")
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//button[text()='确定']").click()
        except:
            pass
        finally:
            time.sleep(2)

    def get_modules(self):
        time.sleep(1)
        text =[]
        modules = self.driver.find_elements_by_xpath("//a[contains(@class,'project-module')]/span")
        for i in range(len(modules)):
            text.append(modules[i].text)
        return text


    def build_project(self, project_name):
        driver = self.driver
        self.wait_until_clickable("//button[text()='新建项目']")
        self.wait_until_visible("//input[@name='projectName']")
        article = driver.find_element_by_xpath("//input[@name='projectName']")
        driver.find_element_by_xpath("//input[@name='projectName']").clear()
        ActionChains(driver).double_click(article).perform()
        driver.find_element_by_xpath("//input[@name='projectName']").send_keys(project_name)
       # driver.find_element_by_xpath("//input[@name='companyName']").send_keys('1')
        #driver.find_element_by_xpath("//input[@name='companyAddress']").send_keys('1')
       # driver.find_element_by_xpath("//input[@name='postalCode']").send_keys('310000')
       # driver.find_element_by_xpath("//input[@name='name']").send_keys('1')
       # driver.find_element_by_xpath("//input[@name='department']").send_keys('1')
      #  driver.find_element_by_xpath("//input[@name='officePhone']").send_keys('1')
        time.sleep(2)
        driver.find_element_by_xpath("//button[text()='储存']").click()
        time.sleep(1)
        #driver.find_element_by_xpath("//*[@id='index']/div/div[2]/div[1]/ol/li[1]").click()
        #time.sleep(2)
        return project_navigation(driver=self.driver)

    def cancel_build_project(self, project_name):
        driver = self.driver
        self.wait_until_clickable("//button[text()='新建项目']")
        self.wait_until_visible("//input[@name='projectName']")
        article = driver.find_element_by_xpath("//input[@name='projectName']")
        driver.find_element_by_xpath("//input[@name='projectName']").clear()
        ActionChains(driver).double_click(article).perform()
        driver.find_element_by_xpath("//input[@name='projectName']").send_keys(project_name)
        driver.find_element_by_xpath("//input[@name='companyName']").send_keys('1')
        driver.find_element_by_xpath("//input[@name='companyAddress']").send_keys('1')
        driver.find_element_by_xpath("//input[@name='postalCode']").send_keys('310000')
        driver.find_element_by_xpath("//input[@name='name']").send_keys('1')
        driver.find_element_by_xpath("//input[@name='department']").send_keys('1')
        driver.find_element_by_xpath("//input[@name='officePhone']").send_keys('1')

    def start_project(self):
        self.wait_until_clickable("//button[text()='新建项目']")

    def input_project(self, infos):
        driver = self.driver
        time.sleep(2)
        article = driver.find_element_by_xpath("//input[@name='projectName']")
        driver.find_element_by_xpath("//input[@name='projectName']").clear()
        ActionChains(driver).double_click(article).perform()
        driver.find_element_by_xpath("//input[@name='projectName']").send_keys(infos[0])
        driver.find_element_by_xpath("//input[@name='companyName']").clear()
        driver.find_element_by_xpath("//input[@name='companyName']").send_keys(infos[1])
        driver.find_element_by_xpath("//input[@name='companyAddress']").clear()
        driver.find_element_by_xpath("//input[@name='companyAddress']").send_keys(infos[2])
        driver.find_element_by_xpath("//input[@name='postalCode']").clear()
        driver.find_element_by_xpath("//input[@name='postalCode']").send_keys(infos[3])
        driver.find_element_by_xpath("//input[@name='name']").clear()
        driver.find_element_by_xpath("//input[@name='name']").send_keys(infos[4])
        driver.find_element_by_xpath("//input[@name='department']").clear()
        driver.find_element_by_xpath("//input[@name='department']").send_keys(infos[5])
        driver.find_element_by_xpath("//input[@name='officePhone']").clear()
        driver.find_element_by_xpath("//input[@name='officePhone']").send_keys(infos[6])

    def save_disable(self):
        try:
            self.driver.find_element_by_xpath("//button[text()='储存' and @disabled='disabled']")
            return True
        except:
            return False

    def cancel_build(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[text()='取消']").click()
        time.sleep(1)

    def exit_build(self):
        self.wait_until_clickable("//button[text()='离开']")

    def back_to_build(self):
        self.wait_until_clickable("//button[text()='返回编辑']")

    def build_default_name_project(self):
        driver = self.driver
        self.wait_until_clickable("//button[text()='新建项目']")
        time.sleep(0.5)
        driver.find_element_by_xpath("//input[@name='companyName']").send_keys('1')
        driver.find_element_by_xpath("//input[@name='companyAddress']").send_keys('1')
        driver.find_element_by_xpath("//input[@name='postalCode']").send_keys('310000')
        driver.find_element_by_xpath("//input[@name='name']").send_keys('1')
        driver.find_element_by_xpath("//input[@name='department']").send_keys('1')
        driver.find_element_by_xpath("//input[@name='officePhone']").send_keys('1')
        time.sleep(2)
        driver.find_element_by_xpath("//button[text()='储存']").click()
        time.sleep(0.3)
        #driver.find_element_by_xpath("//*[@id='index']/div/div[2]/div[1]/ol/li[1]").click()
        #time.sleep(2)
        try:
            driver.find_element_by_xpath("//div[contains(@class, 'toast-message')]")
            return True
        except:
            time.sleep(2)
            return False

    def build_multiarea_project(self, project_name, number_of_area, area_name):
        driver = self.driver
        self.wait_until_clickable("//button[text()='新建项目']")
        self.wait_until_visible("//input[@name='projectName']")
        article = driver.find_element_by_xpath("//input[@name='projectName']")
        driver.find_element_by_xpath("//input[@name='projectName']").clear()
        ActionChains(driver).double_click(article).perform()
        driver.find_element_by_xpath("//input[@name='projectName']").send_keys(project_name)
        driver.find_element_by_xpath("//input[@name='companyName']").send_keys('1')
        driver.find_element_by_xpath("//input[@name='companyAddress']").send_keys('1')
        driver.find_element_by_xpath("//input[@name='postalCode']").send_keys('310000')
        driver.find_element_by_xpath("//input[@name='name']").send_keys('1')
        driver.find_element_by_xpath("//input[@name='department']").send_keys('1')
        driver.find_element_by_xpath("//input[@name='officePhone']").send_keys('1')
        for i in range(number_of_area):
            self.wait_until_clickable("//button[@ng-click='infoCtrl.addZone()']")
            time.sleep(2)
            self.driver.find_elements_by_xpath("//input[contains(@ng-model,'zone')]")[i+1].click()
            self.driver.find_elements_by_xpath("//input[contains(@ng-model,'zone')]")[i+1].send_keys(area_name[i])
        time.sleep(2)
        driver.find_element_by_xpath("//button[text()='储存']").click()
        time.sleep(1)
        #driver.find_element_by_xpath("//*[@id='index']/div/div[2]/div[1]/ol/li[1]").click()
        #time.sleep(2)
        return project_navigation(driver=self.driver)

    def delete_project(self, project_name):
        driver = self.driver
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='搜索']").send_keys(project_name)
        self.wait_until_clickable("//button[@ng-click='projectCtrl.setMultipleEditTrue()']")
        self.wait_until_clickable("//div[@class='project-item-image']")
        self.wait_until_clickable("//button[@ng-click='projectCtrl.delete()']")
        self.wait_until_clickable("//button[@ng-click='confirmCtrl.ok()']")

    def search_project(self, project_name):
        driver = self.driver
        driver.refresh()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='搜索']").send_keys(project_name)
        try:
            self.driver.find_element_by_xpath("//div[@class='project-item-image']")
            return True
        except:
            return False

    def edit_project(self):
        driver = self.driver
        time.sleep(0.5)
        driver.find_element_by_xpath("//button[@ng-click='projectCtrl.setMultipleEditTrue()']").click()
        time.sleep(0.5)

    def select_project(self):
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//div[@class='project-item-image']").click()
        time.sleep(0.5)

    def clear_selection(self):
        self.wait_until_clickable("//button[@ng-click='projectCtrl.clearSelected()']")

    def cancel_edit(self):
        self.wait_until_clickable("//button[@ng-click='projectCtrl.setMultipleEditFalse()']")

    def del_button(self):
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath("//button[@ng-click='projectCtrl.delete()']")
            return True
        except:
            return False

    def get_current_page(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath("//span[@class='section-title']").text

    def check_area_default_name(self, project_name):
        self.driver.refresh()
        self.driver.find_element_by_xpath("//input[@placeholder='搜索']").send_keys(project_name)
        self.wait_until_clickable("//div[@class='project-item-image']")
        self.wait_until_clickable("//button[text()='编辑']")
        self.wait_until_clickable("//button[@ng-click='infoCtrl.addZone()']")
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath("//input[contains(@class,'ng-invalid')]")
            return True
        except:
            return False

    def check_del_button(self):
        time.sleep(1)
        self.driver.find_element_by_xpath()
        try:
            self.driver.find_element_by_xpath("//button[text()='批量删除']")
            return True
        except:
            return False

    def quit(self):
        driver = self.driver    # 关闭浏览器
        driver.quit()

    def wait_until_clickable(self, xpath):
        for i in range(0, 30):
            try:
                self.driver.find_element_by_xpath(xpath).click()
                break
            except:
                time.sleep(0.5)

    # 检测到元素存在
    def wait_until_visible(self, xpath):
        for i in range(0, 30):
            try:
                self.driver.find_element_by_xpath(xpath)
                break
            except:
                time.sleep(0.5)


class project_navigation:
    def __init__(self, driver):
        self.driver = driver

    def goto_basic_info(self):
        self.wait_until_clickable("//span[text()='基本信息']")
        return Basic_info(driver=self.driver)

    def goto_asset_analysis(self):
        self.wait_until_clickable("//span[text()='资产分析']")
        return Asset_analysis(driver=self.driver)

    def goto_threat_analysis(self):
        self.wait_until_clickable("//span[text()='威胁分析']")
        return Threat_analysis(driver=self.driver)

    def goto_traffic_analysis(self):
        self.wait_until_clickable("//span[text()='流量分析']")
        return Traffic_analysis(driver=self.driver)

    def goto_reports(self):
        self.wait_until_clickable("//span[text()='报告管理']")
        return Reports(driver=self.driver)

    def goto_project_manager(self):
        self.wait_until_clickable("//span[text()='项目管理']")
        return project_manager

    def goto_system_setup(self, selection):
        self.wait_until_clickable("//div[@class='logout']")
        # options = ['账户管理','系统设置','无线设置','版本信息','系统升级']
        self.wait_until_clickable("//a[text()='%s']" % selection)
        time.sleep(0.5)
        return System_setup(driver=self.driver)
    
    def quit(self):
        driver = self.driver    # 关闭浏览器
        driver.quit()

    def wait_until_clickable(self, xpath):
        for i in range(0, 30):
            try:
                self.driver.find_element_by_xpath(xpath).click()
                break
            except:
                time.sleep(0.5)

    # 检测到元素存在
    def wait_until_visible(self, xpath):
        for i in range(0, 30):
            try:
                self.driver.find_element_by_xpath(xpath)
                break
            except:
                time.sleep(0.5)

    def find_ele(self, xpath):
        time.sleep(1)
        self.driver.find_element_by_xpath(xpath)
        time.sleep(1)


class Basic_info(project_navigation):
    def begin(self):
        self.wait_until_visible("//div[text()='项目基本信息']")

# ==================================                Action                  =====================================

    def edit_project(self):
        self.find_ele("//span[text()='项目基本信息']")
        self.wait_until_clickable("//button[contains(@ng-click,'infoCtrl.MODE_EDIT')]")

    def rename_project(self, new_name):
        self.driver.find_element_by_xpath("//input[@name='projectName']").clear()
        self.driver.find_element_by_xpath("//input[@name='projectName']").send_keys(new_name)

    def add_area(self, new_name):
        self.wait_until_clickable("//button[contains(@ng-click,'nfoCtrl.addZone')]")
        inputs = self.driver.find_elements_by_xpath("//div[contains(@class,'area-set')]//input")
        inputs[len(inputs)-1].clear()
        inputs[len(inputs)-1].send_keys(new_name)

    def change_infos(self, info_set):
        alist = []
        if type(info_set) is type('string'):
            alist.append(info_set)
        elif type(info_set) is type(['alist']):
            alist = info_set
        info_field = self.driver.find_elements_by_xpath("//input[@type='text']")
        for i in range(len(alist)):
            if len(alist[i])>0:
                info_field[i].clear()
                info_field[i].send_keys(alist[i])

    def save_change(self):
        self.wait_until_clickable("//button[@ng-click='infoCtrl.saveProject()']")

    def cancel_change(self):
        self.wait_until_clickable("//button[@ng-click='infoCtrl.open()']")
        self.wait_until_clickable("//button[@ng-click='confirmCtrl.ok()']")

# ==================================                delete                  =====================================

    def del_area(self, area_index):
        self.find_ele("//span[text()='项目基本信息']")
        area_keys = self.driver.find_elements_by_xpath("//button[contains(@ng-click,'infoCtrl.cancel')]")
        area_keys[area_index].click()
        self.find_ele("//button[@ng-click='confirmCtrl.ok()']")
        self.wait_until_clickable("//button[@ng-click='confirmCtrl.ok()']")

# ==================================                Check                  =====================================
    def get_area_name(self, area_index):
        self.find_ele("//span[text()='项目基本信息']")
        areas = self.driver.find_elements_by_xpath("//input[contains(@ng-model,'zone.$value')]")
        try:
            name = areas[area_index].get_attribute("value")
            return name
        except:
            return False

    def get_info(self):
        time.sleep(1)
        # info = {'project_name':'', 'company':'', 'address':'', 'postcode':'', 'contacts':'', 'department':'', 'phone':''}
        info = []
        values = self.driver.find_elements_by_xpath("//h5[contains(@ng-if,'infoCtrl')]")
        for i in range(len(values)):
            info.append(values[i].text)
        return info

    def check_cancel_pop_window(self):
        self.wait_until_clickable("//button[@ng-click='infoCtrl.open()']")
        text = self.driver.find_element_by_xpath("//div[@class='ng-binding']").text
        self.wait_until_clickable("//button[@ng-click='confirmCtrl.ok()']")
        self.find_ele("//span[@class='section-title' and text()='项目基本信息']")
        return text

# ==================================                Alert                  =====================================

    def get_alert(self):
        time.sleep(0.5)
        try:
            msg = self.driver.find_element_by_xpath("//div[contains(@class, 'toast-message')]").text
            return msg
        except:
            return ''

    def project_name_alert(self):
        time.sleep(0.5)
        try:
            msg = self.driver.find_element_by_xpath("//div[contains(@class, 'toast-message')]").text
            return msg
        except:
            return None


class Asset_analysis(project_navigation):
    def begin(self):
        pass

    def refresh_page(self):
        self.driver.refresh()
        time.sleep(4)

    def manul_entry(self, area='默认区域名称', method='手动录入资产'):
        time.sleep(1)
        self.wait_until_clickable("//button[@ng-click='assetCtrl.startEntry()']")
        #self.driver.find_element_by_xpath("//button[@ng-click='assetCtrl.startEntry()']")
        #self.wait_until_clickable("//button[@ng-click='assetCtrl.startEntry()']")
        self.wait_until_clickable("//form[@name='assetAnalysisForm']//div[contains(.,'资产分析区域')]//i[1]")
        self.find_ele("//a[contains(@ng-click,'zone') and contains(.,'%s')]" % area)
        self.wait_until_clickable("//a[contains(@ng-click,'zone') and contains(.,'%s')]" % area)
        self.wait_until_clickable("//form[@name='assetAnalysisForm']//div[contains(.,'填写方式')]//i[1]")
        self.find_ele("//a[contains(@ng-click,'entryType') and contains(.,'%s')]" % method)
        self.wait_until_clickable("//a[contains(@ng-click,'entryType') and contains(.,'%s')]" % method)
        self.wait_until_visible("//div[@class='modal-content']")
        self.wait_until_clickable("//button[@ng-click='entryCtrl.ok()']")

    def auto_entry(self, scan_port, ip_address):
        self.wait_until_clickable("//button[@ng-click='assetCtrl.startEntry()']")
        time.sleep(1)
        self.wait_until_clickable("//span[contains(., '手动录入资产')]")
        self.wait_until_clickable("//li[contains(., '自动识别资产')]")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='scanPortIp']").click()
        self.driver.find_element_by_xpath("//input[@name='scanPortIp']").send_keys(scan_port)
        self.driver.find_element_by_xpath("//input[@name='ipAddress']").click()
        self.driver.find_element_by_xpath("//input[@name='ipAddress']").send_keys(ip_address)
        time.sleep(1)
        self.wait_until_clickable("//button[@ng-click='entryCtrl.ok()']")
        for i in range(1, 10):
            try:
                self.driver.find_element_by_xpath("//div[contains(@class, 'toast-message')]")
                return False
            except:
                time.sleep(0.5)

        for i in range(1, 200):
            try:
                self.driver.find_element_by_xpath("//span[text()='资产列表']")
                break
            except:
                time.sleep(1)

    def get_area_name(self):
        self.find_ele("//div[@class='name' and text()='资产录入表']")
        area_name = self.driver.find_element_by_xpath("//div[@class='scope']//p").text
        return area_name

    def check_title_row(self):
        self.find_ele("//div[@class='name' and text()='资产录入表']")
        keys = self.driver.find_elements_by_xpath("//tr[@class='titlerow']//th[contains(@class,'col-sm')]")
        alist=[]
        for i in range(len(keys)):
            alist.append(json.dumps(keys[i].text))
        return alist


    def asset_entry_byname(self, area_name):
        self.wait_until_clickable("//button[@ng-click='assetCtrl.startEntry()']")
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='资产分析设置']")
        self.wait_until_clickable("//div[contains(., '资产分析区域')]//span[contains(@class, 'textOverflow')]")
        self.wait_until_clickable("//a[contains(@ng-click,'zone') and text()='%s']" % area_name)
        self.wait_until_clickable("//button[@ng-click='entryCtrl.ok()']")
        self.wait_until_clickable("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceTypeModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[text()='数据服务器（DB）']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceVendorModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[text()='Fox Software']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceNameModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[text()='VFP']")
        self.wait_until_clickable("//button[contains(., '完成录入')]")
        time.sleep(1)

    def get_area_name_from_dropdown(self):
        name_list=[]
        self.find_ele("//button[@ng-click='assetCtrl.startEntry()']")
        self.wait_until_clickable("//button[@ng-click='assetCtrl.startEntry()']")
        self.wait_until_clickable("//form[@name='assetAnalysisForm']//div[contains(.,'资产分析区域')]//i[1]")
        time.sleep(1)
        areas = self.driver.find_elements_by_xpath("//a[contains(@ng-click,'zone')]")
        number = len(areas)
        for i in range(number-1):
            name_list.append(areas[i+1].text)
        self.wait_until_clickable("//button[contains(@ng-click,'entryCtrl.cancel')]")
        return name_list

    def check_autocomplete(self):
        result = True
        self.wait_until_clickable("//span[@ng-click='listCtrl.addNewDevice()']")
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@ng-model='manualCtrl.deviceTypeModel']//input").send_keys('DB')
        try:
            self.driver.find_element_by_xpath("//a[contains(@ng-bind-html, 'match.label') and contains(., 'DB')]").click()
        except:
            result = False
        self.driver.find_element_by_xpath("//div[@addons='manualCtrl.addVendor']//input").send_keys('IBM')
        try:
            self.driver.find_element_by_xpath("//a[contains(@ng-bind-html, 'match.label') and contains(., 'IBM')]").click()
        except:
            result = False
        return result

    def check_autoscan_message(self):
        result = True
        self.wait_until_clickable("//div[@ng-click='listCtrl.goTomanager()']")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@ng-click='assetCtrl.startEntry()']")
        self.wait_until_clickable("//button[@ng-click='assetCtrl.startEntry()']")
        self.wait_until_clickable("//span[contains(., '手动录入资产')]")
        self.wait_until_clickable("//li[contains(., '自动识别资产')]")
        try:
            self.driver.find_element_by_xpath("//div[@class='form-group' and contains(.,'资产分析区域')]//div[text()='此区域已有资产分析']")
        except:
            result = False
        try:
            self.driver.find_element_by_xpath("//div[@class='form-group' and contains(.,'填写方式')]//div[text()='每次执行扫描都将覆盖之前存在的，具有同样IP地址的资产信息。']")
        except:
            result = False
        try:
            self.driver.find_element_by_xpath("//span[text()='请正确输入扫描口IP!']")
        except:
            result = False
        try:
            self.driver.find_element_by_xpath("//span[text()='请正确输入扫描范围，详情请查看右侧帮助！']")
        except:
            result = False
        finally:
            self.wait_until_clickable("//button[@ng-click='entryCtrl.cancel()' and text()='取消']")
            return result

    def cancellation_of_assetentry(self):
        self.wait_until_clickable("//button[@ng-click='assetCtrl.startEntry()']")
        self.wait_until_clickable("//button[@ng-click='entryCtrl.ok()']")
        self.wait_until_clickable("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//span[text()='返回']")
        self.wait_until_clickable("//button[@ng-click='confirmCtrl.ok()']")
        self.wait_until_clickable("//span[text()='返回']")
        try:
            time.sleep(2)
            self.driver.find_element_by_xpath("//button[text()='开始录入']")
            print "true test"
            return True
        except:
            return False

    def asset_autoscan(self, ip_address):
        self.wait_until_clickable("//button[@ng-click='assetCtrl.startEntry()']")
        time.sleep(1)
        self.wait_until_clickable("//span[contains(., '手动录入资产')]")
        self.wait_until_clickable("//li[contains(., '自动识别资产')]")
        self.driver.find_element_by_xpath("//input[@name='ipAddress']").send_keys(ip_address)
        result = True
        try:
            self.driver.find_element_by_xpath("//button[@ng-click='entryCtrl.ok()' and @disabled='disabled']")
        except:
            result = False
        finally:
            self.wait_until_clickable("//button[@ng-click='entryCtrl.cancel()' and text()='取消']")
            return result

    def jump_to_threat(self, option):
        time.sleep(2)
        self.wait_until_clickable("//span[text()='威胁分析']")
        self.wait_until_clickable("//button[text()='%s']" % option)
        time.sleep(2)

    def cancel_autoscan(self, scan_port, subnet_ip):
        self.wait_until_clickable("//button[@ng-click='assetCtrl.startEntry()']")
        time.sleep(1)
        self.wait_until_clickable("//span[contains(., '手动录入资产')]")
        self.wait_until_clickable("//li[contains(., '自动识别资产')]")
        self.wait_until_clickable("//input[@name='scanPortIp']")
        self.driver.find_element_by_xpath("//input[@name='scanPortIp']").send_keys(scan_port)
        self.wait_until_clickable("//input[@name='ipAddress']")
        self.driver.find_element_by_xpath("//input[@name='ipAddress']").send_keys(subnet_ip)
        time.sleep(0.5)
        self.wait_until_clickable("//button[@ng-click='entryCtrl.ok()']")
        time.sleep(5)
        self.wait_until_clickable("//i[@ng-click='topologyCtrl.openRunPanel()']")
        time.sleep(0.5)
        self.wait_until_clickable("//button[text()='取消']")
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//i[@ng-click='topologyCtrl.openRunPanel()']")
            return True
        except:
            return False
        finally:
            self.wait_until_clickable("//i[@ng-click='topologyCtrl.openRunPanel()']")
            time.sleep(0.5)
            self.wait_until_clickable("//button[@ng-click='confirmCtrl.ok()' and text()='停止']")

    def stop_autoscan(self,  scan_port, subnet_ip):
        self.wait_until_clickable("//button[@ng-click='assetCtrl.startEntry()']")
        time.sleep(1)
        self.wait_until_clickable("//span[contains(., '手动录入资产')]")
        self.wait_until_clickable("//li[contains(., '自动识别资产')]")
        self.wait_until_clickable("//input[@name='scanPortIp']")
        self.driver.find_element_by_xpath("//input[@name='scanPortIp']").click()
        self.driver.find_element_by_xpath("//input[@name='scanPortIp']").send_keys(scan_port)
        self.wait_until_clickable("//input[@name='ipAddress']")
        self.driver.find_element_by_xpath("//input[@name='ipAddress']").click()
        self.driver.find_element_by_xpath("//input[@name='ipAddress']").send_keys(subnet_ip)
        time.sleep(0.5)
        self.wait_until_clickable("//button[@ng-click='entryCtrl.ok()']")
        self.wait_until_clickable("//i[@ng-click='topologyCtrl.openRunPanel()']")
        self.wait_until_clickable("//button[text()='停止']")
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//button[@ng-click='assetCtrl.startEntry()']")
            return True
        except:
            return False

    def stop_save_autoscan(self, scan_port, subnet_ip):
        self.wait_until_clickable("//button[@ng-click='assetCtrl.startEntry()']")
        self.wait_until_clickable("//span[contains(., '手动录入资产')]")
        self.wait_until_clickable("//li[contains(., '自动识别资产')]")
        self.wait_until_clickable("//input[@name='scanPortIp']")
        self.driver.find_element_by_xpath("//input[@name='scanPortIp']").click()
        self.driver.find_element_by_xpath("//input[@name='scanPortIp']").send_keys(scan_port)
        self.wait_until_clickable("//input[@name='ipAddress']")
        self.driver.find_element_by_xpath("//input[@name='ipAddress']").click()
        self.driver.find_element_by_xpath("//input[@name='ipAddress']").send_keys(subnet_ip)
        time.sleep(0.5)
        self.wait_until_clickable("//button[@ng-click='entryCtrl.ok()']")
        self.wait_until_clickable("//i[@ng-click='topologyCtrl.openRunPanel()']")
        self.wait_until_clickable("//button[text()='停止并保存']")
        time.sleep(0.3)
        try:
            self.driver.find_element_by_xpath("//div[@class='blocker_there_finished ng-scope']")
            return True
        except:
            return False

    def action_autoscan(self, option):
        self.wait_until_clickable("//i[contains(@ng-click,'openRunPanel')]")
        self.wait_until_clickable("//button[contains(@ng-click,'confirmCtrl') and contains(.,'%s')]" % option)

    def add_device(self, vendor='Fox Software',  model='VFP', device_type='数据服务器（DB）', ip_address='9.9.9.9', link=False):
        time.sleep(1)
        self.wait_until_clickable("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceTypeModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[contains(.,'%s')]" % device_type)
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceVendorModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//div[@class='form-group' and contains(.,'厂商')]//a[contains(.,'%s')]" % vendor)
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceNameModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[contains(.,'%s')]" % model)
        self.wait_until_clickable("//input[@ng-model='manualCtrl.ip']")
        self.driver.find_element_by_xpath("//input[@ng-model='manualCtrl.ip']").send_keys(ip_address)
        time.sleep(2)
        if link:
            self.wait_until_clickable("//button[@ng-click='manualCtrl.addAssociateZone()']")
            self.wait_until_clickable("//div[contains(@ng-repeat,'Associate_info')]//span[contains(@on-toggle,'open')]")
            self.wait_until_clickable("//a[contains(@ng-click,'selectZone')]")
        self.wait_until_clickable("//button[contains(., '完成录入')]")
        time.sleep(1)

    def add_device_with_link(self, vendor='Fox Software',  model='VFP', device_type='数据服务器（DB）', ip_address='9.9.9.9', ipaddress_1='1.1.1.1'):
        time.sleep(1)
        self.wait_until_clickable("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceTypeModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[contains(.,'%s')]" % device_type)
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceVendorModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//div[@class='form-group' and contains(.,'厂商')]//a[contains(.,'%s')]" % vendor)
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceNameModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[contains(.,'%s')]" % model)
        self.wait_until_clickable("//input[@ng-model='manualCtrl.ip']")
        self.driver.find_element_by_xpath("//input[@ng-model='manualCtrl.ip']").send_keys(ip_address)
        time.sleep(2)
        self.wait_until_clickable("//button[@ng-click='manualCtrl.addAssociateZone()']")
        self.wait_until_clickable("//div[contains(@ng-repeat,'Associate_info')]//span[contains(@on-toggle,'open')]")
        self.wait_until_clickable("//a[contains(@ng-click,'selectZone')]")
        time.sleep(1)
        self.wait_until_clickable("//input[@name='ipAddress_1']")
        self.driver.find_element_by_xpath("//input[@name='ipAddress_1']").send_keys(ipaddress_1)
        time.sleep(1)
        self.wait_until_clickable("//button[contains(., '完成录入')]")

    def add_device_without_area(self, vendor='Fox Software',  model='VFP', device_type='数据服务器（DB）', ip_address='9.9.9.9', ipaddress_1='1.1.1.1'):
        time.sleep(1)
        self.wait_until_clickable("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceTypeModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[contains(.,'%s')]" % device_type)
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceVendorModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//div[@class='form-group' and contains(.,'厂商')]//a[contains(.,'%s')]" % vendor)
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceNameModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[contains(.,'%s')]" % model)
        self.wait_until_clickable("//input[@ng-model='manualCtrl.ip']")
        self.driver.find_element_by_xpath("//input[@ng-model='manualCtrl.ip']").send_keys(ip_address)
        time.sleep(2)
        self.wait_until_clickable("//button[@ng-click='manualCtrl.addAssociateZone()']")

    def check_button_disable(self):
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//button[contains(., '完成录入') and @disabled='disabled']")
            return True
        except:
            return False

    def add_plc(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@ng-click='assetCtrl.startEntry()']")
        self.wait_until_clickable("//button[@ng-click='assetCtrl.startEntry()']")
        time.sleep(1)
        self.wait_until_clickable("//button[@ng-click='entryCtrl.ok()']")
        self.wait_until_clickable("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceTypeModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[text()='可编程逻辑控制器（PLC）']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceVendorModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[text()='西门子（Siemens）']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceNameModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[text()='S7-300']")
        self.wait_until_clickable("//button[contains(., '完成录入')]")
        time.sleep(1)

    def add_specific(self, vendor,  model, ip_address='9.9.9.9', device_type ='未知类型'):
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceTypeModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[text()='%s']" %device_type)
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceVendorModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[contains(.,'添加厂商')]")
        time.sleep(2)
        self.wait_until_clickable("//div[@class='form-group' and contains(.,'厂商中文名称')]//input")
        self.driver.find_element_by_xpath("//div[@class='form-group' and contains(.,'厂商中文名称')]//input").send_keys(vendor)
        self.wait_until_clickable("//div[@class='form-group' and contains(.,'厂商英文名称')]//input")
        self.driver.find_element_by_xpath("//div[@class='form-group' and contains(.,'厂商英文名称')]//input").send_keys(vendor)
        self.wait_until_clickable("//button[contains(@ng-click,'newVendor') and contains(.,'储存')]")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceNameModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[contains(.,'添加型号')]")
        time.sleep(2)
        self.wait_until_clickable("//div[@class='form-group' and contains(.,'设备型号名称')]//input")
        self.driver.find_element_by_xpath("//div[@class='form-group' and contains(.,'设备型号名称')]//input").send_keys(model)
        self.wait_until_clickable("//button[contains(@ng-click,'newDeviceName') and contains(.,'储存')]")
        self.wait_until_clickable("//input[@ng-model='manualCtrl.ip']")
        self.driver.find_element_by_xpath("//input[@ng-model='manualCtrl.ip']").send_keys(ip_address)
        self.wait_until_clickable("//button[contains(., '完成录入')]")
        self.wait_until_clickable("//div[@class='name' and text()='资产录入表']")
        self.find_ele("//div[@class='name' and text()='资产录入表']")

    def modify_device(self, vendor, device_model, device_type='未知类型', index=0):
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='name' and text()='资产录入表']")
        devices = self.driver.find_elements_by_xpath("//i[@ng-click='listCtrl.editDevice(val.device_id)']")
        devices[index].click()
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceTypeModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[text()='%s']" % device_type)
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceVendorModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[contains(.,'%s')]" % vendor)
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceNameModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[contains(.,'%s')]" % device_model)
        self.wait_until_clickable("//button[contains(., '完成录入')]")

    def check_undifined(self, vendor, device_type):
        time.sleep(1)
        self.wait_until_clickable("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceTypeModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[contains(.,'%s')]" % device_type)
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceVendorModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[contains(.,'%s')]" % vendor)
        self.find_ele("//div[contains(@addons, 'addVendor')]//input")
        self.driver.find_element_by_xpath("//div[contains(@addons, 'addVendor')]//input").clear()
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceVendorModel']//span[@class='input-group-btn']")
        self.find_ele("//a[contains(.,'%s')]" % vendor)
        try:
            self.find_ele("//a[contains(.,'%s')]" % 'undefined')
            return False
        except:
            return True

    def check_all_device_version(self):
        self.find_ele("//div[@class='name' and text()='资产录入表']")
        alist = self.driver.find_elements_by_xpath("//i[contains(@ng-click,'listCtrl.editDevice')]")
        versions = []
        for i in range(len(alist)):
            self.driver.find_elements_by_xpath("//i[contains(@ng-click,'listCtrl.editDevice')]")[i].click()
            info_read = self.get_device_info()
            versions.append(info_read)
            self.wait_until_clickable("//span[contains(.,'返回')]")
            self.wait_until_clickable("//button[contains(@ng-click,'confirmCtrl.ok')]")
            time.sleep(2)
        return versions

    def get_device_info(self):
        infos=[]
        self.find_ele("//div[@class='name ng-binding' and text()='编辑设备']")
        infos.append(self.driver.find_element_by_xpath("//div[contains(@ng-model,'manualCtrl.deviceTypeModel')]//input").get_attribute("value"))
        infos.append(self.driver.find_element_by_xpath("//div[contains(@ng-model,'manualCtrl.deviceVendorModel')]//input").get_attribute("value"))
        infos.append(self.driver.find_element_by_xpath("//div[contains(@ng-model,'manualCtrl.deviceNameModel')]//input").get_attribute("value"))
        infos.append(self.driver.find_element_by_xpath("//input[contains(@ng-model,'manualCtrl.version')]").get_attribute("value"))
        infos.append(self.driver.find_element_by_xpath("//input[contains(@ng-model,'manualCtrl.ip')]").get_attribute("value"))
        return infos

    def cancel_add_device(self):
        self.find_ele("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//a[contains(@class,'project-module') and contains(.,'资产分析')]")
        self.wait_until_clickable("//button[text()='取消']")
        self.find_ele("//div[@class='name ng-binding' and text()='添加设备']")
        self.wait_until_clickable("//a[contains(@class,'project-module') and contains(.,'资产分析')]")
        self.wait_until_clickable("//button[text()='确定']")
        try:
            self.find_ele("//span[@class='section-title' and text()='资产分析']")
            return True
        except:
            return False

    def search_device(self, device_name):
        self.find_ele("//div[@class='name' and text()='资产录入表']")
        self.driver.find_element_by_xpath("//input[@placeholder='搜寻']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='搜寻']").send_keys(device_name)

    def check_device_info(self, key_info):
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='name' and text()='资产录入表']")
        self.wait_until_clickable("//tr[@class='inforow ng-scope' and contains(@ng-repeat,'listCtrl.devices')]//td[contains(@title,'%s')]" %key_info)
        try:
            self.driver.find_element_by_xpath("//tr[@class='inforow ng-scope' and contains(@ng-repeat,'listCtrl.devices')]//td[contains(@title,'%s')]" % key_info)
            return True
        except:
            return False

    def check_vendor_selection(self, vendor):
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='name' and text()='资产录入表']")
        self.wait_until_clickable("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceTypeModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[text()='未知类型']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceVendorModel']//span[@class='input-group-btn']")
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//a[@ng-click='onSelect(op)' and contains(.,'%s')]" % vendor)
            return True
        except:
            return False

    def duplicate_device_entry(self, vendor, device_type ='未知类型'):
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceTypeModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[text()='%s']" % device_type)
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceVendorModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[contains(.,'添加厂商')]")
        time.sleep(2)
        self.wait_until_clickable("//div[@class='form-group' and contains(.,'厂商中文名称')]//input")
        self.driver.find_element_by_xpath("//div[@class='form-group' and contains(.,'厂商中文名称')]//input").send_keys(vendor)
        self.wait_until_clickable("//div[@class='form-group' and contains(.,'厂商英文名称')]//input")
        self.driver.find_element_by_xpath("//div[@class='form-group' and contains(.,'厂商英文名称')]//input").send_keys(vendor)
        self.wait_until_clickable("//button[contains(@ng-click,'newVendor') and contains(.,'储存')]")
        try:
            self.find_ele("//div[contains(@class, 'toast-message') and text()='该厂商已经存在.']")
            return True
        except:
            return False

    def ip_conflict_message(self, vendor, type, ip_address):
        self.wait_until_clickable("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceTypeModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[text()='可编程逻辑控制器（PLC）']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceVendorModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[text()='西门子（Siemens）']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceNameModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[text()='S7-300']")
        self.wait_until_clickable("//input[@ng-model='manualCtrl.ip']")
        self.driver.find_element_by_xpath("//input[@ng-model='manualCtrl.ip']").send_keys(ip_address)
        self.wait_until_clickable("//button[contains(., '完成录入')]")
        try:
            self.driver.find_elements_by_xpath("//div[contains(@class, 'toast-message') and text()='该ip已经存在.']")
            return True
        except:
            return False

    def switch_sort_type(self,type):
        if type == 1:
            self.wait_until_clickable("//button[contains(@ng-click,'setReportStyle') and contains(@ng-click,'square')]")
        else:
            self.wait_until_clickable("//button[contains(@ng-click,'setReportStyle') and contains(@ng-click,'tableRow')]")


    def asset_exist(self, area_name='默认区域名称'):
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//div[@class='asset-item-text']//h5[@title='%s资产分析']" % area_name).click()
            return True
        except:
            return False

    def vulner_detail_button(self):
        try:
            self.find_ele("//div[@ng-click='listCtrl.goAssetDetail(val)' and contains(.,'漏洞详情')]")
            return True
        except:
            return False

    def vulnerability_detail(self):
        self.wait_until_clickable("//button[@ng-click='listCtrl.calculateScore()']")
        time.sleep(3)
        self.driver.find_element_by_xpath("//i[@ng-click='listCtrl.detailReport()']").click()
        self.wait_until_clickable("//td[contains(@ng-click,'goAssetDetail(device)')]")
        self.driver.find_element_by_xpath("//div[@class='modal-title' and text()='设备详情细节']")
        self.wait_until_clickable("//button[@class='close']")
        time.sleep(1)
        self.wait_until_clickable("//td[contains(@ng-click,'goVulnerabilityDetail(vul)') and contains(.,'详情')]")
        result = False
        try:
            self.driver.find_element_by_xpath("//div[contains(@ng-class,'vulnerability.ThreatLevel')]")
            result = True
        except:
            result = False
        finally:
            self.wait_until_clickable("//i[@ng-click='vulInfoCtrl.close()']")
            self.wait_until_clickable("//button[@ng-click='reportCtrl.closePage()']")
            return result

    def enter_vulner_detail(self):
        self.find_ele("//div[@class='name' and text()='资产录入表']")
        self.wait_until_clickable("//td[contains(@ng-click,'goAssetDetail(val)')]")

    def check_vulner_detail(self,key_info):
        self.find_ele("//div[contains(@class,'modal-title')]")
        try:
            self.driver.find_element_by_xpath("//div[@ng-if='detailCtrl.selectedData' and contains(.,'%s')]" % key_info)
            return True
        except:
            return False

    def get_device_detail(self):
        lists =[]
        self.find_ele("//div[@class='dialogMid']")
        details = self.driver.find_elements_by_xpath("//div[@class='dialogMid']//span")
        for detail in details:
            lists.append(detail.text)
        return lists

    def close_vulner_page(self):
        self.wait_until_clickable("//button[@ng-click='detailCtrl.close()']")

    def try_to_del(self):
        self.wait_until_clickable("//span[contains(., '更多操作')]")
        self.wait_until_clickable("//span[contains(., '删除')]")

    def modify_vendor(self, type, vendor_name, old_verdor):
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='name' and text()='资产录入表']")
        self.wait_until_clickable("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceTypeModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[text()='%s']" % type)
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceVendorModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[contains(.,'编辑厂商列表')]")
        self.wait_until_clickable("//input[@placeholder='搜寻']")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='搜寻']").send_keys(old_verdor)
        time.sleep(1)
        self.wait_until_clickable("//i[@ng-click='confirmCtrl.editVendor(key)']")
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//input[@id='newVendorCh']").clear()
        self.driver.find_element_by_xpath("//input[@id='newVendorCh']").send_keys(vendor_name)
        self.driver.find_element_by_xpath("//input[@id='newVendorEn']").clear()
        self.driver.find_element_by_xpath("//input[@id='newVendorEn']").send_keys(vendor_name)
        self.wait_until_clickable("//i[contains(@ng-click,'confirmCtrl.currentDeviceVendor')]")
        self.wait_until_clickable("//button[contains(@ng-click,'confirmCtrl.retrunData')]")
        self.wait_until_clickable("//span[text()='返回']")
        self.wait_until_clickable("//button[text()='确定']")

    def del_vendor(self, vendor_name, type='未知类型'):
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='name' and text()='资产录入表']")
        self.wait_until_clickable("//span[@ng-click='listCtrl.addNewDevice()']")
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceTypeModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[text()='%s']" % type)
        self.wait_until_clickable("//div[@ng-model='manualCtrl.deviceVendorModel']//span[@class='input-group-btn']")
        self.wait_until_clickable("//a[contains(.,'编辑厂商列表')]")
        self.wait_until_clickable("//input[@placeholder='搜寻']")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='搜寻']").send_keys(vendor_name)
        time.sleep(1)
        self.wait_until_clickable("//i[@ng-click='confirmCtrl.delete(key)']")
        self.wait_until_clickable("//button[@ng-click='confirmCtrl.ok(confirmCtrl.retrunData)' and text()='储存']")
        self.wait_until_clickable("//span[text()='返回']")
        self.wait_until_clickable("//button[text()='确定']")

    def del_device_confirmation(self, device_name=''):
        self.wait_until_clickable("//span[contains(., '更多操作')]")
        self.find_ele("//input[contains(@class,'searchInput')]")
        self.driver.find_element_by_xpath("//input[contains(@class,'searchInput')]").clear()
        self.driver.find_element_by_xpath("//input[contains(@class,'searchInput')]").send_keys(device_name)
        self.wait_until_clickable("//input[@id='checkboxInput_all']")
        self.wait_until_clickable("//span[contains(., '删除')]")
        self.wait_until_clickable("//button[@ng-click='confirmCtrl.ok()']")
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath("//div[@class='inforow ng-scope']").click()
            time.sleep(1)
            return False
        except:
            return True

    def del_device_from_edit(self, device_name):
        self.find_ele("//input[contains(@class,'searchInput')]")
        self.driver.find_element_by_xpath("//input[contains(@class,'searchInput')]").clear()
        self.driver.find_element_by_xpath("//input[contains(@class,'searchInput')]").send_keys(device_name)
        self.wait_until_clickable("//i[@ng-click='listCtrl.editDevice(val.device_id)']")
        self.wait_until_clickable("//button[@ng-click='manualCtrl.deleteDevice()']")
        self.wait_until_clickable("//button[text()='确定']")

    def del_asset_analysis(self, area_name='默认区域名称'):
        self.wait_until_clickable("//button[text()='批量操作']")
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='asset-item-text']//h5[@title='%s资产分析']" % area_name)
        self.wait_until_clickable("//div[@class='asset-item-text']//h5[@title='%s资产分析']" % area_name)
        self.wait_until_clickable("//button[@ng-click='assetCtrl.delete()']")
        self.wait_until_clickable("//button[text()='确定']")
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//div[@class='asset-item-text']//h5[@title='%s资产分析']" % area_name)
            return False
        except:
            return True

    def calculate_score(self):
        self.find_ele("//button[contains(@ng-click,'calculateScore') and contains(.,'计算威胁评分')]")
        self.wait_until_clickable("//button[contains(@ng-click,'calculateScore') and contains(.,'计算威胁评分')]")
        time.sleep(5)

    def get_score(self):
        time.sleep(2)
        try:
            points = self.driver.find_element_by_xpath("//span[contains(@ng-if, 'system_score')]").text
            return points
        except:
            return False

    def go_back(self):
        self.find_ele("//span[text()='返回']")
        try:
            self.driver.find_element_by_xpath("//i[@class='circleButtoner fa fa-arrow-left']").click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath("//button[text()='停止并保存']").click()
        except:
            pass
        time.sleep(1)

    #资产拓扑界面的返回
    def asets_topology_go_back(self):
        try:
            self.driver.find_element_by_xpath("//i[@class='circleButtoner smallcircle fa fa-arrow-left']").click()
        except:
            pass
        time.sleep(1)


    def discard_page(self):
        # self.wait_until_clickable("//a[@ng-click='projectCtrl.returnProjects()' and contains(.,'项目管理')]")
        self.driver.back()
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//button[@ng-click='confirmCtrl.ok()']").click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath("//button[@ng-click='reportCtrl.closePage()']").click()
        except:
            pass

    def topology(self):
        self.find_ele("//div[@class='icon' and contains(.,'资产拓扑')]")
        self.wait_until_clickable("//div[@class='icon' and contains(.,'资产拓扑')]")
        time.sleep(2)

    def get_subnet_in_topology(self):
        self.find_ele("//span[@class='small' and text()='扫描网段： ']")
        result = self.driver.find_element_by_xpath("//span[@class='small' and text()='扫描网段： ']//em").text
        return result

    def get_number_of_device_with_compeleted_info(self):
        self.find_ele("//span[@class='small' and text()='扫描网段： ']")
        result = self.driver.find_element_by_xpath("//span[@id='discovered_number']").text
        return result

    def analysis_topology(self):
        driver = self.driver
        ip_list = driver.find_elements_by_xpath("//*[contains(@id,'_result')]")
        for ip in ip_list:
            print 'success'

    def score_overview(self):
        self.find_ele("//div[@class='icon' and contains(.,'评分总览')]")
        self.wait_until_clickable("//div[@class='icon' and contains(.,'评分总览')]")
        time.sleep(2)

    def check_info_in_score_overview(self, key_info):
        try:
            self.driver.find_element_by_xpath("//div[contains(@class,'asset-report fixed-container') and contains(.,'%s')]" % key_info)
            return True
        except:
            return False

    def find_ip_in_topology(self, ip):
        try:
            self.driver.find_element_by_xpath("//div[@class='busSVG' and contains(.,'%s')]" % ip)
            return True
        except:
            return False

    def get_score_in_topology(self):
        self.find_ele("//span[@class='small' and text()='扫描网段： ']")
        score = self.driver.find_element_by_xpath("//span[contains(@ng-if,'topologyCtrl.scanResult.meta.system_score')]").text
        return score

    def get_number_of_devices_in_topology(self):
        try:
            result = self.driver.find_element_by_xpath("//span[@id='completed_number']//em").text
            return result
        except:
            return False

    def find_device_in_topology(self, device_name):
        self.find_ele("//span[contains(@ng-if,'topologyCtrl.scanResult')]")
        try:
            self.find_ele("//div[@class='scan-body' and contains(.,'%s')]" % device_name)
            return True
        except:
            return False

    def find_device_in_score_overview(self, device_name):
        self.find_ele("//div[@class='score-header' and contains(.,'资产分析评分')]")
        try:
            self.find_ele("//div[@class='chart-xaxis' and contains(.,'%s')]" % device_name)
            self.wait_until_clickable("//button[@ng-click='reportCtrl.closePage()']")
            return True
        except:
            return False

    def find_device_in_top5_threat(self, device_name):
        time.sleep(5)
        self.find_ele("//div[@class='score-header' and contains(.,'资产分析评分')]")
        try:
            self.find_ele("//div[@class='main-content-table' and contains(.,'高威胁评分设备')]//td[contains(.,'%s')]" % device_name)
            return True
        except:
            return False

    def find_vulnerability_CVE(self):
        time.sleep(5)
        self.find_ele("//div[@class='score-header' and contains(.,'资产分析评分')]")
        self.wait_until_clickable("//tr[contains(@ng-repeat,'vulnerabilityList')]")
        result = True
        try:
            self.find_ele("//span[contains(.,'CVE-2012-2559')]")
        except:
            return False
        finally:
            self.wait_until_clickable("//i[@ng-click='vulInfoCtrl.close()']")
            return result

    def count_vulnerability_in_top5_threat(self):
        table = self.driver.find_elements_by_xpath("//tr[contains(@ng-repeat,'vulnerabilityList')]")
        return len(table)


    def check_error_msg(self):
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath("//div[contains(@class, 'toast-message')]")
            return True
        except:
            return False

    def get_current_page(self, title):
        try:
            self.find_ele("//span[@class='section-title' and text()='%s']" % title)
            return True
        except:
            return False

    def goto_project_manager(self):
        print '1'
        self.wait_until_clickable("//span[text()='项目管理']")
        print '2'
        return project_manager


class Threat_analysis(project_navigation):
    def begin(self):
        self.wait_until_clickable("//span[text()='开始']")

    def fill_questionnaire(self, answer):
        time.sleep(2)
        question_block_list = self.driver.find_elements_by_xpath("//div[@class='leftNav']/ul/li")
        question_catagory_xpath = "//div[@class='quesBoxContains greyBoxScroller']//ul[@ng-repeat='score in threatEditCtrl.scoreData track by $index']"
        for question_block in question_block_list:
            #uncomment here
            question_block.click()
            time.sleep(2)
            question_catagorys = self.driver.find_elements_by_xpath(question_catagory_xpath)
            for question_catagory in question_catagorys:
                question_title_clickables = question_catagory.find_element_by_xpath(".//li[1]")
                # print 'find all div'
                question_title_clickables = question_title_clickables.find_elements_by_xpath(".//span[@class='checkItem']//div")
                if len(question_title_clickables) == 0:
                    question_bodys = question_catagory.find_elements_by_xpath(".//li[contains(@class,'pointer ng-scope')]")
                    question_body_clickables = question_bodys[0].find_elements_by_xpath(".//span[@class='checkItem']//div[@class='radioBox']")
                    question_body_clickables[answer].click()
                else:
                    question_title_clickable = question_title_clickables[answer]
                    question_title_clickable.click()


# =======================================Before Start Filling==========================================================


    def enter_form(self, form_name, action='start'):
        if action is 'start':
            self.wait_until_clickable("//div[@class='quesItem ng-scope' and contains(., '%s')]//span[text()='开始']" % form_name)
        elif action is 'continue':
            self.wait_until_clickable("//div[@class='quesItem ng-scope' and contains(., '%s')]//span[text()='继续编辑']" % form_name)
        elif action is 'reset':
            self.wait_until_clickable("//div[@class='quesItem ng-scope' and contains(., '%s')]//span[text()='重新编辑']" % form_name)
            self.wait_until_clickable("//button[@ng-click='confirmCtrl.ok()']")
        time.sleep(1)
        des = self.driver.find_element_by_xpath("//span[@class='keyData ng-binding']").text
        return des

    def sele_sort(self, key_word):
        self.find_ele("//span[@class='section-title' and text()='威胁分析']")
        self.wait_until_clickable("//button[contains(@class,'btn-dropdown')]")
        self.wait_until_clickable("//a[contains(@ng-click,'changeOrder(choice)') and contains(.,'%s')]" % key_word)

    def get_form_names(self):
        self.find_ele("//span[@class='section-title' and text()='威胁分析']")
        name_list =[]
        forms = self.driver.find_elements_by_xpath("//div[@class='quesInfo']//div[contains(@class,'bigger')]")
        for i in range(len(forms)):
            name_list.append(forms[i].text)
        return name_list

    def reset_form(self,form_name):
        self.find_ele("//span[@class='section-title' and text()='威胁分析']")
        self.wait_until_clickable("//div[@class='quesItem ng-scope' and contains(., '%s')]//span[text()='清空重填']" % form_name)
        self.wait_until_clickable("//button[@ng-click='confirmCtrl.ok()']")

    def enter_report(self, form_name):
        self.find_ele("//span[@class='section-title' and text()='威胁分析']")
        self.wait_until_clickable("//div[@class='quesItem ng-scope' and contains(., '%s')]//span[text()='查看结果']" % form_name)
        try:
            self.find_ele("//div[@class='score-header' and contains(.,'威胁分析评分')]")
            return True
        except:
            return False

    def check_form_status(self, form_name):
        self.find_ele("//div[@class='bigger ng-binding' and contains(.,'%s')]" % form_name)
        result = False
        try:
            self.find_ele("//div[@class='quesItem ng-scope' and contains(.,'%s')]//div[@class='progressInfo ng-scope']" % form_name)
            result = 'processing'
        except:
            pass
        try:
            self.find_ele("//div[@class='quesItem ng-scope' and contains(.,'%s')]//span[text()='开始']" % form_name)
            result = 'blank'
        except:
            pass
        finally:
            return result

    def check_form_complete(self):
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//span[contains(@class,'rotateText') and text()='已完成']")
            return True
        except:
            return False

    def get_precentage(self,form_name):
        time.sleep(1)
        precentage = self.driver.find_element_by_xpath("//div[contains(.,'%s')]//span[text()='已完成']//i" % form_name).text
        return precentage

    def check_name(self, form_name):
        self.find_ele("//span[@class='section-title' and text()='威胁分析']")
        return self.driver.find_element_by_xpath("//div[@class='quesInfo' and contains(.,'%s')]//div[contains(@class,'bigger')]"%form_name).text

    def check_update_time(self, form_name):
        self.find_ele("//div[@class='quesItem ng-scope' and contains(.,'%s')]//div[@class='progressInfo ng-scope']" % form_name)
        return self.driver.find_element_by_xpath("//div[@class='quesInfo' and contains(.,'%s')]//div[contains(.,'上次更新')]" % form_name).text

    def check_description(self, form_name):
        self.find_ele("//span[@class='section-title' and text()='威胁分析']")
        return self.driver.find_element_by_xpath("//div[@class='quesInfo' and contains(.,'%s')]//div[contains(@class,'desc')]" %form_name).text


# ==================================================Filling questions===============================================


    def select_sub_title(self, title):
        self.find_ele("//div[@class='content']")
        self.wait_until_clickable("//ul[@class='greyBoxScroller']//span[contains(.,'%s')]" % title)

    def fill_questions_in_current_page(self, answer='yes'):
        self.find_ele("//div[@class='content']")
        subs = self.driver.find_elements_by_xpath("//div[contains(@ng-click,'score.sub_group') and contains(@ng-click,'%s')]//label" % answer)
        for sub in subs:
            sub.click()
            time.sleep(1)

    def fill_a_question(self, answer='yes'):
        self.wait_until_clickable("//div[@class='radioBox' and contains(@ng-click,'%s')]//label" % answer)

    def get_question_comment(self, index):
        other = self.driver.find_elements_by_xpath("//span[@class='checkItem']//div[@class='radioBox' and contains(@ng-click,'alt')]")
        other[index-1].click()
        add_comment = self.driver.find_elements_by_xpath("//span[@class='checkItem']//div[@class='editBtn']")
        add_comment[index-1].click()
        time.sleep(2)
        result = self.driver.find_element_by_xpath("//textarea[@placeholder='请填写评论']").get_attribute('value')
        return result

    def fill_question(self, index, choice='yes', comment='anything'):
        self.find_ele("//li[@class='sub']")
        # sub = self.driver.find_elements_by_xpath("//li[@class='sub']")
        # question = sub[lv2].find_elements_by_xpath("//li[contains(@ng-repeat,'sub_group.questions')]")
        if choice is 'else':
            other = self.driver.find_elements_by_xpath("//span[@class='checkItem']//div[@class='radioBox' and contains(@ng-click,'alt')]")
            other[index-1].click()
            add_comment = self.driver.find_elements_by_xpath("//span[@class='checkItem']//div[@class='editBtn']")
            add_comment[index-1].click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//textarea[@placeholder='请填写评论']").send_keys(comment)
            self.wait_until_clickable("//i[contains(@ng-click,'closeSiderBar')]")
        else:
            answer = self.driver.find_elements_by_xpath("//span[@class='checkItem']//div[@class='radioBox' and contains(@ng-click,'%s')]" % choice)
            answer[index].click()

    def question_examination(self, index):
        time.sleep(1)
        other = self.driver.find_elements_by_xpath("//span[@class='checkItem']//i[contains(@class,'pencil')]")
        other[index-1].click()
        time.sleep(2)
        self.wait_until_clickable("//span[contains(@ng-click,'threatEditCtrl.saveExamination')]//label")
        self.wait_until_clickable("//i[@ng-click='threatEditCtrl.closeSiderBar()']")
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//span[@class='checkItem']//text[contains(@class,'light_color_grey')]")
            return True
        except:
            return False

    def fill_and_change_level(self):
        self.wait_until_clickable("//div[@id='questionBox']//li[@class='sub']//div[1][@class='radioBox']/label")
        self.wait_until_clickable("//i[@ng-click='threatEditCtrl.setLevel()']")
        self.find_ele("//span[@title='请选择评估等级']")
        self.wait_until_clickable("//span[@title='请选择评估等级']")
        self.wait_until_clickable("//a[contains(@title, '调度管理系统')]")
        self.wait_until_clickable("//button[text()='开始']")
        self.find_ele("//span[contains(@class, 'keyLevel') and contains(.,'调度端系统2级')]")
        self.wait_until_clickable("//span[text()='返回']")
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath("//div[@class='quesItem ng-scope' and contains(., '电力监控系统')]//span[text()='继续编辑']")
            return True
        except:
            return False

    def change_level(self, level, system):
        self.wait_until_clickable("//i[@ng-click='threatEditCtrl.setLevel()']")
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[contains(@class,'dropDownBox')]").click()
        self.wait_until_clickable("//a[contains(@title, '%s')]" % level)
        time.sleep(0.5)
        try:
            tar = self.driver.find_elements_by_xpath("//span[contains(@class,'textOverflow')]")
            time.sleep(0.5)
            tar[1].click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//a[contains(@ng-click,'levelSetCtrl') and contains(.,'%s')]" % system).click()
        except:
            pass
        time.sleep(1)
        self.wait_until_clickable("//button[text()='开始']")
        time.sleep(2)
        try:
            lv = self.driver.find_element_by_xpath("//span[contains(@class, 'keyLevel')]").text
            return lv
        except:
            return False

    def goto_subtitle(self):
        self.wait_until_clickable("//span[text()='信息安全组织机构']")
        return self.driver.find_element_by_xpath("//div[@class='title ng-binding']").text

    def fill_and_reset(self):
        self.wait_until_clickable("//div[@id='questionBox']//li[@class='sub']//div[1][@class='radioBox']/label")
        self.wait_until_clickable("//span[text()='清空当前']")
        self.wait_until_clickable("//button[text()='确定']")
        time.sleep(0.5)
        self.wait_until_clickable("//span[text()='返回']")
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath("//div[@class='quesItem ng-scope' and contains(., '工业控制系统信息安全评估规范')]//span[text()='开始']")
            return True
        except:
            return False

    def reset_current_page(self):
        self.wait_until_clickable("//span[text()='清空当前']")
        self.wait_until_clickable("//button[text()='确定']")

    def check_commit(self):
        self.driver.refresh()
        for i in range(1, 10):
            try:
                self.driver.find_element_by_xpath("//span[text()='提交问卷']").click()
                #time.sleep(2)
                #self.driver.find_element_by_xpath("//i[@class='fa fa-times circleButtoner']").click()
                return True
            except:
                time.sleep(1)

        return False


# =======================================In Report Page================================================================


    def get_report_title(self):
        self.find_ele("//div[@class='score-header' and contains(.,'威胁分析评分')]")
        return self.driver.find_element_by_xpath("//span[@class='name ng-binding']").text

    def get_score(self):
        self.find_ele("//div[@class='score-header' and contains(.,'威胁分析评分')]")
        return self.driver.find_element_by_xpath("//span[@class='percent ng-binding']").text

    def get_level(self):
        self.find_ele("//div[@class='score-header' and contains(.,'威胁分析评分')]")
        return self.driver.find_element_by_xpath("//div[@class='box-content safeLevel']//span[contains(@ng-class,'saveLevelColor')]").text

    def get_management_level(self):
        self.find_ele("//div[@class='score-header' and contains(.,'威胁分析评分')]")
        sele = self.driver.find_elements_by_xpath("//div[@class='row' and contains(.,'达标建议')]//span[@class='ng-binding']")
        return sele[0].text

    def get_performance_level(self):
        self.find_ele("//div[@class='score-header' and contains(.,'威胁分析评分')]")
        sele = self.driver.find_elements_by_xpath("//div[@class='row' and contains(.,'达标建议')]//span[@class='ng-binding']")
        return sele[2].text

    def get_number_of_choice(self, choice):
        self.find_ele("//div[@class='score-header' and contains(.,'威胁分析评分')]")
        return self.driver.find_element_by_xpath("//li[contains(.,legendColorBox) and contains(.,'%s')]//span[contains(@class,'legendColorBox')]" % choice).text

    def get_number_of_yes(self):
        self.find_ele("//div[@class='score-header' and contains(.,'威胁分析评分')]")
        return self.driver.find_element_by_xpath("//ul[@class='legend']/li/span").text

    def close_report(self):
        self.find_ele("//div[@class='score-header' and contains(.,'威胁分析评分')]")
        self.wait_until_clickable("//span[contains(@class,'report-close')]//i")

    def go_back(self):
        self.wait_until_clickable("//span[text()='返回']")
        self.find_ele("//span[@class='section-title' and text()='威胁分析']")

    def see_result(self):
        self.wait_until_clickable("//span[text()='查看结果']")
        self.find_ele("//div[@class='score-header' and contains(.,'威胁分析评分')]")

class Traffic_analysis(project_navigation):
    def begin(self):
        self.wait_until_clickable("//span[text()='开始截取数据包']")

    def pacpstart(self):
        self.wait_until_clickable("//button[contains(., '开始截取数据包')]")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name=' minutes']").send_keys('1')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='pcapSize']").send_keys('1')
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@ng-click='trafficCtrl.startIntercept()']").click()
        time.sleep(65)
        try:
            self.driver.find_element_by_xpath("//button[@ng-if='trafficCtrl.totalPcaps']")
            self.driver.find_element_by_xpath("//button[contains(@ng-if, 'completed')]")
            return True
        except:
            return False

    def start_analysis(self, area='默认区域名称'):
        self.wait_until_clickable("//button[@ng-click='trafficMgtCtrl.startEntry()']")
        self.wait_until_clickable("//i[@class='fa fa-angle-down']")
        self.wait_until_clickable("//a[contains(@ng-click,'entryCtrl.changeOrder') and contains(.,'%s')]" % area)
        self.wait_until_clickable("//button[contains(@ng-click,'entryCtrl.ok')]")

    def start_setting(self):
        self.wait_until_clickable("//button[contains(., '开始截取数据包')]")

    def set_parameter(self, hour='', min='', sec='', size=''):
        self.find_ele("//span[contains(.,'当前截取')]")
        self.driver.find_element_by_xpath("//input[@name=' hour']").clear()
        self.driver.find_element_by_xpath("//input[@name=' hour']").send_keys(hour)
        self.driver.find_element_by_xpath("//input[@name=' minutes']").clear()
        self.driver.find_element_by_xpath("//input[@name=' minutes']").send_keys(min)
        self.driver.find_element_by_xpath("//input[@name=' seconds']").clear()
        self.driver.find_element_by_xpath("//input[@name=' seconds']").send_keys(sec)
        self.driver.find_element_by_xpath("//input[@name='pcapSize']").clear()
        self.driver.find_element_by_xpath("//input[@name='pcapSize']").send_keys(size)

    def set_pcap_name(self, pcap_name):
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[contains(@name,'pcapName')]").clear()
        self.driver.find_element_by_xpath("//input[contains(@name,'pcapName')]").send_keys(pcap_name)

    def cancel_setting(self):
        self.wait_until_clickable("//button[contains(@ng-click,'trafficCtrl.setpopupStatus')]")

    def start_intercept(self):
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath("//button[@ng-click='trafficCtrl.startIntercept()']").click()
            return True
        except:
            return False

    def intercept_disable(self):
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath("//button[@ng-click='trafficCtrl.startIntercept()' and @disabled='disabled']").click()
            return True
        except:
            return False

    def stop_intercept(self):
        self.wait_until_clickable("//button[contains(@ng-click,'trafficCtrl.stopIntercept')]")
        time.sleep(7)

    def check_pcap(self):
        try:
            self.find_ele("//td[contains(@class,'traffic-control traffic-control-group')]//button[contains(@ng-if,'completed')]")
            return True
        except:
            return False

    def check_pcap_name(self,name):
        try:
            self.find_ele("//td[contains(@class,'traffic-control traffic-control-group')]//h5[contains(.,'%s')]" % name)
            return True
        except:
            return False

    def get_error_msg(self):
        time.sleep(0.5)
        text = self.driver.find_element_by_xpath("//div[@class='toast-message']").text
        return text


    def go_back(self):
        self.wait_until_clickable("//button[contains(@ng-click,'trafficCtrl.goTomanager')]")

    def goto_page(self, page):
        self.wait_until_clickable("//span[@class='ng-binding' and text()='%s']" % page)
        self.wait_until_clickable("//button[@ng-click='confirmCtrl.ok()' and text()='确定']")
        time.sleep(7)

    def refresh_page(self):
        self.driver.refresh()
        time.sleep(4)

    def analysis_exist(self, area='默认区域名称'):
        self.find_ele("//span[contains(@class,'section-title') and text()='流量分析']")
        try:
            self.driver.find_element_by_xpath("//h5[contains(@title,'%s')]" % area).click()
            return True
        except:
            return False

# =============================   traffic report =======================================
    def go_to_report(self):
        self.wait_until_clickable("//span[text()='流量分析统计']")

    def get_intercept_time(self):
        time.sleep(2)
        res = self.driver.find_element_by_xpath("//div[@class='numInfo' and contains(.,'截取时间总长')]//div[@class='num']/b").text
        return res[-2:-1]

    def close_report(self):
        self.wait_until_clickable("//span[@class='report-close']//button")
        time.sleep(1)


class Reports(project_navigation):
    def begin(self):
        self.wait_until_visible("//div[text()='项目总览']")

    def edit_info(self,title):
        self.find_ele("//span[contains(.,'%s')]//text[contains(@class,'edit')]" % title)
        self.wait_until_clickable("//span[contains(.,'%s')]//text[contains(@class,'edit')]" % title)

    def get_infos(self):
        time.sleep(1)
        list=[]
        inputs = self.driver.find_elements_by_xpath("//input")
        for i in range(len(inputs)):
            value = inputs[i].get_attribute('value')
            list.append(value)
        return list

    def re_enter_infos(self, list):
        time.sleep(1)
        inputs = self.driver.find_elements_by_xpath("//input")
        for i in range(len(list)):
            try:
                inputs[i].clear()
                inputs[i].send_keys(list[i])
                time.sleep(0.5)
            except:
                pass

    def check_threat_report(self, name):
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//div[@class='infoBox' and contains(.,'%s')]" % name)
            return True
        except:
            return False

    def check_traffic_report(self, area_name):
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//div[@class='infoBox bigger' and contains(.,'%s')]" % area_name)
            return True
        except:
            return False

    def confirm_change(self):
        self.wait_until_clickable("//button[text()='确定']")

    def cancel_change(self):
        self.wait_until_clickable("//button[text()='取消']")




class System_setup(project_navigation):
    def begin(self):
        pass

    def get_version(self, section):
        self.driver.find_element_by_xpath("//div[text()='威胁评估平台版本信息']")
        res = self.driver.find_element_by_xpath("//div[@class='modal-verinfo' and contains(., '%s')]//span[@class='span-detail ng-binding']" % section).text
        return res

    def wifi_setup(self):
        self.driver.find_element_by_xpath("//input[@name='ip']").clear()
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//input[@name='ip']").send_keys('0.0.0.0')
        self.wait_until_clickable("//button[@ng-click='wirelessCtrl.save()']")
        time.sleep(0.3)
        try:
            self.driver.find_element_by_xpath("//div[contains(@class, 'toast-message')]")
            return True
        except:
            return False

    def edit_ip_infos(self, infos):
        self.find_ele("//div[text()='系统设置']")
        inputs = self.driver.find_elements_by_xpath("//input[@type='text']")
        for i in range(len(inputs)):
            inputs[i].clear()
            inputs[i].send_keys(infos[i])

    def get_ip_infos(self):
        self.find_ele("//div[text()='系统设置']")
        infos = []
        inputs = self.driver.find_elements_by_xpath("//input[@type='text']")
        for i in range(len(inputs)):
            infos.append(inputs[i].get_attribute('value'))
        return infos

    def cancel_ip_edit(self):
        self.wait_until_clickable("//button[@ng-click='ipCtrl.cancel()']")

    def get_current_page(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath("//span[@class='section-title']").text

    def change_system_ip(self, new_ip):
        self.wait_until_clickable("//div[@class='titlePosition' and text()='系统设置']")
        self.driver.find_element_by_xpath("//div[@class='titlePosition' and text()='系统设置']")
        self.driver.find_element_by_xpath("//div[@class='ipContent' and contains(.,'IP地址')]//input").clear()
        self.driver.find_element_by_xpath("//div[@class='ipContent' and contains(.,'IP地址')]//input").send_keys(new_ip)
        self.wait_until_clickable("//button[@ng-click='ipCtrl.save()']")

    def check_error_msg(self):
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath("//div[contains(@class, 'toast-message')]")
            return True
        except:
            return False

# =====================================================  log  ===================================================
    def check_log_msg(self, project, msg):
        try:
            self.find_ele("//tr[contains(@pagination-id,'logslister') and contains(.,'%s') and contains(.,'%s')]" % (project, msg))
            return True
        except:
            return False

    def search_info(self, key_info):
        self.wait_until_clickable("//input[@placeholder='搜索']")
        self.driver.find_element_by_xpath("//input[@placeholder='搜索']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='搜索']").send_keys(key_info)

    # ===================  account   ======================

    def create_new_account(self, user, pwd):
        self.wait_until_clickable("//button[text()='创建用户']")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[contains(@name,'loginName')]").send_keys(user)
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//input[contains(@name,'newPassword')]").send_keys(pwd)
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//input[contains(@name,'repeatPassword')]").send_keys(pwd)
        self.wait_until_clickable("//button[contains(.,'创建') and contains(@ng-click,'confirmCtrl.ok')]")

    def search_user(self, user):
        self.wait_until_clickable()

    def del_user(self, user):
        time.sleep(1)
        self.wait_until_clickable("//tr[contains(.,'%s')]//i[contains(@ng-click,'deleteuser')]" % user)
        time.sleep(1)
        self.wait_until_clickable("//button[contains(.,'删除用户')]")

    def edit_user(self, user, new_pwd):
        time.sleep(1)
        self.wait_until_clickable("//tr[contains(.,'%s')]//i[contains(@ng-click,'editUser')]" % user)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='newPassword']").send_keys(new_pwd)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='repeatPassword']").send_keys(new_pwd)
        self.wait_until_clickable("//button[text()='确定']")

    def reset_admin(self, oldpwd, newpwd):
        self.wait_until_clickable("//button[@ng-click='usersCtrl.setAdminPsd()']")
        self.wait_until_clickable("//input[@name='oldPassword']")
        self.driver.find_element_by_xpath("//input[@name='oldPassword']").send_keys(oldpwd)
        self.wait_until_clickable("//input[@name='newPassword']")
        self.driver.find_element_by_xpath("//input[@name='newPassword']").send_keys(newpwd)
        self.wait_until_clickable("//input[@name='repeatPassword']")
        self.driver.find_element_by_xpath("//input[@name='repeatPassword']").send_keys(newpwd)
        time.sleep(1)
        self.wait_until_clickable("//button[text()='确定']")

    # =========================== company ================================
    def edit_company_info(self, infos):
        self.wait_until_clickable("//button[@ng-click='usersCtrl.setCompanyInfo()']")
        self.wait_until_clickable("//input[@name='companyName']")
        self.driver.find_element_by_xpath("//input[@name='companyName']").clear()
        self.driver.find_element_by_xpath("//input[@name='companyName']").send_keys(infos[0])
        self.wait_until_clickable("//input[@name='companyAddress']")
        self.driver.find_element_by_xpath("//input[@name='companyAddress']").clear()
        self.driver.find_element_by_xpath("//input[@name='companyAddress']").send_keys(infos[1])
        self.wait_until_clickable("//input[@name='companyCode']")
        self.driver.find_element_by_xpath("//input[@name='companyCode']").clear()
        self.driver.find_element_by_xpath("//input[@name='companyCode']").send_keys(infos[2])

    def yes(self):
        self.wait_until_clickable("//button[text()='确定']")

    def no(self):
        self.wait_until_clickable("//button[text()='取消']")

    def get_company_infos(self):
        self.wait_until_clickable("//button[@ng-click='usersCtrl.setCompanyInfo()']")
        infos = []
        self.wait_until_clickable("//input[@name='companyName']")
        infos.append(self.driver.find_element_by_xpath("//input[@name='companyName']").get_attribute("value"))
        self.wait_until_clickable("//input[@name='companyAddress']")
        infos.append(self.driver.find_element_by_xpath("//input[@name='companyAddress']").get_attribute("value"))
        self.wait_until_clickable("//input[@name='companyCode']")
        infos.append(self.driver.find_element_by_xpath("//input[@name='companyCode']").get_attribute("value"))
        self.wait_until_clickable("//button[text()='取消']")
        return infos

    # ==================== normal user  ======================================
    def edit_normal_user(self, infos):
        self.wait_until_clickable("//button[contains(@ng-click,'userInfoCtrl.changeMode')]")
        time.sleep(1)
        inputs = self.driver.find_elements_by_xpath("//input")
        for i in range(len(infos)):
            inputs[i].clear()
            inputs[i].send_keys(infos[i])
            time.sleep(0.5)
        self.wait_until_clickable("//button[text()=' 存储 ']")

    def reset_normal_pwd(self, oldpwd, newpwd):
        self.wait_until_clickable("//button[@ng-click='userInfoCtrl.setAdminPsd()']")
        self.wait_until_clickable("//input[@name='oldPassword' and @type='password']")
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//input[@name='oldPassword' and @type='password']").send_keys(oldpwd)
        time.sleep(0.5)
        self.wait_until_clickable("//input[@name='newPassword']")
        self.driver.find_element_by_xpath("//input[@name='newPassword']").send_keys(newpwd)
        time.sleep(0.5)
        self.wait_until_clickable("//input[@name='repeatPassword']")
        self.driver.find_element_by_xpath("//input[@name='repeatPassword']").send_keys(newpwd)
        time.sleep(0.5)
        self.wait_until_clickable("//button[text()='确定']")

    def check_success_msg(self):
        try:
            self.find_ele("//div[contains(@class,'toast-message') and contains(.,'成功')]")
            return True
        except:
            return False


    def logout(self):
        self.wait_until_clickable("//span[contains(@class,'glyphicon')]")
        self.wait_until_clickable("//a[contains(@ng-click,'logout()')]")

    def go_back(self):
        self.wait_until_clickable("//button[@ng-click='logsCtrl.goPrePage()']")
        time.sleep(1)