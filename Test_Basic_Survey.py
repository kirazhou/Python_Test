# coding=utf-8
import unittest
import sys
import os
from selenium import webdriver
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class Test_user_management(unittest.TestCase):

    def setUp(self):
        pass
    def test_fill_in_survey(self):

        #logininputUsername
        #login_page = 'http://10.0.60.2'
        login_page = 'http://192.168.20.245'
        test_url = 'http://192.168.20.245/#/projects/567493fa25f1e810c8fed18d/threat_analysis/basic_question/edit'
        driver = webdriver.Chrome()
        driver.implicitly_wait(3) # seconds
        driver.get(login_page)
        driver.maximize_window()
        driver.find_element_by_id('inputUsername').send_keys('admin')
        driver.find_element_by_id('inputPassword').send_keys('admins')
        driver.find_element_by_xpath("//button[contains(@class, 'center btn btn-primary')]").click()

        #get the first report
        #time.sleep(2)

        #建立30个任务
        '''for i in range(0, 30):
            driver.find_element_by_xpath("//span[text()='新建项目']").click()
            time.sleep(0.5)
            driver.find_element_by_xpath("//input[@name='projectName']").clear()
            driver.find_element_by_xpath("//input[@name='projectName']").send_keys(str(i+10))
            driver.find_element_by_xpath("//input[@name='companyName']").send_keys('1')
            driver.find_element_by_xpath("//input[@name='companyAddress']").send_keys('1')
            driver.find_element_by_xpath("//input[@name='postalCode']").send_keys('310000')
            driver.find_element_by_xpath("//input[@name='name']").send_keys('1')
            driver.find_element_by_xpath("//input[@name='department']").send_keys('1')
            driver.find_element_by_xpath("//input[@name='officePhone']").send_keys('1')
            time.sleep(2)
            driver.find_element_by_xpath("//button[@class='btn btn-default orgBtn ng-scope']").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='index']/div/div[2]/div[1]/ol/li[1]").click()
            time.sleep(2)'''

        report_list = driver.find_element_by_xpath("//div[contains(@class, 'reportInfo')]")
        report_list.click()

        #click on thread
        #time.sleep(2)
        driver.find_element_by_xpath('//*[@id="index"]/div/div[2]/div[2]/a[3]/img').click()

        #click on basic survey
        #time.sleep(2)
        driver.find_element_by_xpath("//span[text()='开始']").click()
        #driver.find_element_by_xpath("//*[@id='index']/div/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[4]/span").click()
        #time.sleep(2)
        print 'go to different blocks'
        question_block_list = driver.find_elements_by_xpath("//div[@class='leftNav greyBoxScroller']/ul/li")
        #time.sleep(1)
        print question_block_list

        #question block
            #question catagory
                #question title clickiable
                #question boby clickable

        question_catagory_xpath = "//div[@class='quesBoxContains greyBoxScroller']//ul[@ng-repeat='score in threatEditCtrl.scoreData track by $index']"
        #question_catagory_xpath = "//div[@class='autoBox greyBoxScroller']//ul[@ng-repeat='score in threatEditCtrl.scoreData track by $index']"

        #//div[@class='autoBox greyBoxScroller']/ul[@ng-repeat='score in threatEditCtrl.scoreData track by $index'][1]//li[1]//span[@class='checkItem']//div


        #Please wrap the following for loop to iterate through the question blocks located on the left side

        #uncomment here
        for question_block in question_block_list:
            print 'clicking question_block'

            #uncomment here
            question_block.click()
            time.sleep(2)

            #iterate through all question sections
            #each question section got a title and questions
            #sometimes, there are 4 clickable circles on the title line, and sometimes not
            #each question section got few questions, each question got 4 clickable circules, and sometimes a pencil icon
            #for now, we don't click on the pencil
            question_catagorys = driver.find_elements_by_xpath(question_catagory_xpath)
            for question_catagory in question_catagorys:
                print 'gatagory title'

                print 'find title'
                question_title_clickables = question_catagory.find_element_by_xpath(".//li[1]")
                print 'find all div'
                question_title_clickables = question_title_clickables.find_elements_by_xpath(".//span[@class='checkItem']//div")
                for question_title_clickable in question_title_clickables:
                    print 'click all div'
                    question_title_clickable.click()

                print 'find body'
                question_bodys = question_catagory.find_elements_by_xpath(".//li[contains(@class,'pointer ng-scope')]")
                for question_body in question_bodys:
                    print 'question_body'
                    question_body_clickables = question_body.find_elements_by_xpath(".//span[@class='checkItem']//div[@class='radioBox ng-scope']")
                    for quesiton_body_clickable in question_body_clickables:
                        print 'click all div'
                        quesiton_body_clickable.click()


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
