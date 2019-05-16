#!/usr/bin/env python

import time
from selenium import webdriver

# TODO context manager を使って書き直す
class ShadowBrowser():
    def __init__(self,
                 driver_path='./drivers/chromedriver_mac',
                 phantom=False):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.phantom=phantom
        self.open_tabs = {}
    
    def open(self, url):
        self.driver.get(url)
        # self.open_tabs[0] = self.driver.window_handles[0]

    def close(self):
        self.driver.delete_all_cookies()
        self.driver.quit()

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def switch_to_frame(self, frame):
        return self.driver.switch_to_frame(frame)

    def get_attribute(self, attribute):
        return self.driver.get_attribute(attribute)

    def wait(self, seconds=5):
        time.sleep(seconds)

    def save_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)
        
if __name__ == '__main__':
    #b = Browser('/Users/soichi/Projects/finance-integration/bin/chromedriver')
    b = Browser('/Users/sishida/Projects/finance-chart-scraper/lib/drivers/chromedriver_mac')    
    b.open('https://www.google.com/')
    time.sleep(10)
    b.close()
    
