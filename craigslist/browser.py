import time
from selenium.webdriver.support import expected_conditions as EC

import undetected_chromedriver as uc

# from fake_useragent import UserAgent
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options as ChromeOptions
#
# options = ChromeOptions()
#
# # options.add_argument('--headless')
# options.add_argument("--incognito")
# options.add_argument("--nogpu")
# options.add_argument("--disable-gpu")
# options.add_argument("--window-size=1280,1280")
# options.add_argument("--no-sandbox")
# options.add_argument("--enable-javascript")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument('--disable-blink-features=AutomationControlled')
#
# driver_location = '/usr/bin/chromedriver'
# binary_location = '/usr/bin/google-chrome'
#
# options.binary_location = binary_location


import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CraigslistBrowser:
    driver = None

    def __init__(self):
        self.driver = uc.Chrome()

    def visit(self, url):
        time.sleep(random.uniform(3.0, 5.0))
        self.driver.get(url)

    def show_source(self, wait=False):
        if wait:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#search-results-page-1 > ol > div')))

        return self.driver.execute_script("return document.documentElement.outerHTML")

    def quit(self):
        self.driver.quit()
