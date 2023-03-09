import os
import time

from fake_useragent import UserAgent
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()

options.add_argument('--headless')
options.add_argument("--incognito")
options.add_argument("--nogpu")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280,1280")
options.add_argument("--no-sandbox")
options.add_argument("--enable-javascript")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')

ua = UserAgent()
userAgent = ua.random


import random



class CraigslistBrowser:

    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.maximize_window()

    def visit(self, url):
        time.sleep(random.uniform(1.0, 5.1))
        self.driver.get(url)


    def show_source(self):
        return self.driver.page_source

    def quit(self):
        self.driver.quit()

