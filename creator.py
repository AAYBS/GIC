from selenium import webdriver
from base import *
import unittest


class IssueCreator(unittest.TestCase):

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

    def create_issue(self):
        self.driver.get(self.config.get('ISSUES', 'URL'))
        login = LoginPage(self.driver) 
        # print("Opened Login Page")
        login.fill_sign_in()
        # print("FIlled the credentials")
        # print("Logged in")
        ci = IssuesPage(self.driver)
        ci.create_issue()
        # print("Issue Created")
        #close browser
        ci.close()
        # print("Browser Closed")

if __name__ == "__main__":
    ic = IssueCreator()
    ic.create_issue()
