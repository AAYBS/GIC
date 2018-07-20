from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *


class BasePage(object):
    """Base class to initialize the base page that will be called from pages"""

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, uri):
        url = self.base_url + uri


class IssuesPage(BasePage):
    """Issues page action methods come here. in our e.g . Github/issues.com"""


class LoginPage(BasePage):
    """Login page action methods come here. in our e.g . Github/login.com"""

    def __init__(self, driver):
        self.locators = LoginPageLocators
        super(LoginPage, self).__init__(driver)

    def fill_sign_in(self):
        self.find_element(*self.locators.SIGN_IN).click()