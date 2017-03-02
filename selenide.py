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
