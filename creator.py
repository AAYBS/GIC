import configparser
import unittest

from selenium import webdriver

from base import *
import unittest
import configparser

class IssueCreator(unittest.TestCase):

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.driver = webdriver.Firefox()
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.start_page_url = self.config.get('URL', 'START_PAGE_URL')

    def create_issue(self):
        self.driver.get(self.get_url_from_config())
        login = LoginPage(self.driver)
        login.fill_sign_in()
        ci = IssuesPage(self.driver)
        ci.create_issue()
        #close browser
        ci.close()

    def get_url_from_config(self):
        self.config.read('config.ini')
        return self.config['URL']['DEFAULT_URL']


if __name__ == "__main__":
    ic = IssueCreator()
    ic.create_issue()
