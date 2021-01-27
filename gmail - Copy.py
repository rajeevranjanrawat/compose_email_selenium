from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import glob, os, shutil

path = 'D:/Healthworks_QC/Datalake/Automated_QC/client/competitorAnalysis/'
month = 'Jan'

  # Path where your files are at the moment



class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.email = 'rajeevranjanrawat'
        self.password = 'dobarapuchna'
        self.driver = webdriver.Chrome(executable_path="../../../driver/chromedriver.exe")

        #self.driver = webdriver.Chrome("C:/Users/rajeev.ranjan.7QUBE/PycharmProjects/tableau/driver/chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        url = 'https://www.google.com/intl/en-GB/gmail/about/#'
        # driver = webdriver.Chrome("C:/Users/rajeev.ranjan.7QUBE/Downloads/chromedriver.exe")
        self.driver.get(url)
        action = ActionChains(self.driver)

        self.driver.maximize_window()

    def test_app_dynamics_job(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/ul[1]/li[2]/a').click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        #passs email address
        self.driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(self.email)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
        # pass password
        self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()

        print('successfully loged in')


        #click on compose button

        self.driver.find_element_by_xpath('//*[@id=":nj"]/div/div').click()

        #enter the email address for to ,cc & bcc
        to = 'test@gmail.com'
        bcc = 'test1@gmail.com'
        cc = 'test2@gmail.com'
        self.driver.find_element_by_xpath('//*[@id=":tc"]').send_keys(self.to)
        #click on cc
        self.driver.find_element_by_xpath('//*[@id=":ty"]').click()
        self.driver.find_element_by_xpath('//*[@id=":td"]').send_keys(self.cc)
        # click on cc
        self.driver.find_element_by_xpath('//*[@id=":ua"]').click()
        self.driver.find_element_by_xpath('//*[@id=":te"]').send_keys(self.bcc)

        #add subject
        subject = 'this is test email'
        self.driver.find_element_by_xpath('//*[@id=":r9"]').send_keys(self.subject)
        # add subject
        body = 'HI Sir, This is test email to test the scnerio' \
               'Thanks & Regards'
        self.driver.find_element_by_xpath('//*[@id=":q4"]').send_keys(self.body)

        # send

        self.driver.find_element_by_xpath('//*[@id=":rj"]').click()





        time.sleep(30)
        self.driver.close()

    def is_element_present(self, how, what):
            try:
                    self.driver.find_element(by=how, value=what)
            except NoSuchElementException as e:
                    return False
            return True

    def is_alert_present(self):
            try:
                    self.driver.switch_to.alert()
            except NoAlertPresentException as e:
                    return False
            return True

    def close_alert_and_get_its_text(self):
            try:
                    alert = self.driver.switch_to.alert()
                    alert_text = alert.text
                    if self.accept_next_alert:
                            alert.accept()
                    else:
                            alert.dismiss()
                    return alert_text
            finally:
                    self.accept_next_alert = True

    def tearDown(self):

            self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":

        unittest.main()



