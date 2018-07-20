from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *
from base import *
import unittest


class IssueCreator(unittest.TestCase):

    def __init__(self):
        self.driver = webdriver.Firefox()

    def create_issue(self):
        self.driver.get('https://github.com/ZoranPandovski/al-go-rithms/issues')
        login = LoginPage(self.driver)
        login.fill_sign_in()
        ci = IssuesPage(self.driver)
        ci.create_issue()

if __name__ == "__main__":
    ic = IssueCreator()
    ic.create_issue()
