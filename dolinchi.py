#!/usr/bin/env python3

from selenium import webdriver

import time


class Chilindo(object):
    """docstring for Chilindo"""

    def __init__(self, usr, pwd):
        self.err = ''
        self.usr = usr
        self.pwd = pwd
        self.login()

    def beat(self, url, price, sel=0):
        self.driver.get("http://www.chilindo.com/vn/product/%s" % url)
        self.driver.find_element_by_id('ContentPlaceHolder1_txtBidNew').clear()
        self.driver.find_element_by_id(
            'ContentPlaceHolder1_txtBidNew').send_keys(price)
        self.driver.find_element_by_id(
            'ContentPlaceHolder1_ddlRelatedItems').click()

        time.sleep(2)
        self.driver.find_element_by_id('ContentPlaceHolder1_btnBid').click()

    def login(self):
        self.driver = webdriver.Firefox()
        # caps = webdriver.DesiredCapabilities.FIREFOX.copy()
        # driver = webdriver.Remote(desired_capabilities=caps)
        self.driver.get('http://www.chilindo.com')
        try:
            self.driver.find_element_by_id('lnkSelectCountry').click()
            time.sleep(1)
            self.driver.find_element_by_id('popsignin').click()
            time.sleep(1)
            self.driver.find_element_by_id('mutedlogin').click()
            time.sleep(1)
            self.driver.find_element_by_id(
                'Signin1_txtEmail').send_keys(self.usr)
            self.driver.find_element_by_id(
                'Signin1_txtPassword').send_keys(self.pwd)
            time.sleep(1)
            self.driver.find_element_by_id('Signin1_btnSignIn').click()
        except:
            self.err = 'can not login'


def main():
    # profile = webdriver.FirefoxProfile(profile_path)
    # profile = webdriver.FirefoxProfile("/home/hoanghai/.mozilla/firefox/sakntkwa.chilindo/")
    # print(profile)
    # driver = webdriver.Firefox(firefox_profile=profile)
    # driver = webdriver.Firefox(firefox_profile='/home/hoanghai/.mozilla/firefox/sakntkwa.chilindo')
    # fp = webdriver.FirefoxProfile.path()
    # print(profile)
    # set something on the profile...
    # driver = webdriver.Firefox(firefox_profile=fp)
    chi = Chilindo('hoanghaikgs', 'xxx')
    time.sleep(1)
    chi.beat('42-036', 200, 1)
    # url = 'http://www.chilindo.com/vn/product/41-030'
    # price = 130
    # beat(driver, url, price)
    # driver = webdriver.Firefox()
    # driver.get("http://www.python.org")


if __name__ == '__main__':
    main()
