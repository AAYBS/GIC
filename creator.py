from selenium import webdriver
from base import *
import unittest
import ConfigParser

class IssueCreator(unittest.TestCase):

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.config = ConfigParser.ConfigParser()
        self.config.read("config.ini")
        self.issuesURL = self.config.get('ISSUES', 'URL')

    def create_issue(self):
        self.driver.get(self.issuesURL)
        login = LoginPage(self.driver)
        login.fill_sign_in()
        ci = IssuesPage(self.driver)
        ci.create_issue()
        #close browser
        ci.close()

if __name__ == "__main__":
    ic = IssueCreator()
    ic.create_issue()
