"""
Copyright 2017 Raul Alvarez

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Selenide:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1920, 1080)
        self.browser.implicitly_wait(10)
        self.wait = WebDriverWait(self.browser, 10)

    def click(self, location):
        element = self.wait.until(expected_conditions.element_to_be_clickable(location))
        element.click()
        return element

    def click_link_text(self, text):
        return self.click((By.LINK_TEXT, text))

    def click_anchor_tag_href(self, href):
        return self.click_xpath("//a[@href='{}']".format(href))

    def click_xpath(self, xpath):
        return self.click((By.XPATH, xpath))

    def quit(self):
        self.browser.close()
