from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage():
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

    def fill_sign_in(self):
        self.find_element(LoginPageLocators.SIGN_IN).click()










'''
browser = webdriver.Firefox()

browser.get('https://github.com/ZoranPandovski/al-go-rithms/issues')
sign_in = browser.find_element_by_link_text('Sign in')
sign_in.click()

user_name = browser.find_element_by_id('login_field')
password = browser.find_element_by_id('password')
user_name.send_keys('zoran.pandovski@gmail.com')
password.send_keys('220682zpp')
sign_in1 = browser.find_element_by_name('commit')
sign_in1.click()

link = browser.find_element_by_link_text(
    'Add new algorithm, data structure, puzzle, cipher')
link.click()

close_issue = browser.find_elements_by_class_name('js-comment-and-button')
# close_issue.click()


new_issue = browser.find_element_by_link_text('New issue')
new_issue.click()

wait = WebDriverWait(browser, 20)

title_input = wait.until(
    EC.presence_of_element_located((By.ID, 'issue_title')))
title_input.send_keys('Test')

description_input = wait.until(
    EC.presence_of_element_located((By.ID, 'issue_body')))
description_input.clear()
description_input.send_keys('Test 1')

# labels are second element
labels_btn = browser.find_elements_by_class_name('discussion-sidebar-heading')[
    1]
labels_btn.click()

labels_list = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-label-name="bug"]')))

browser.execute_script("arguments[0].click();", labels_list)
# actions = ActionChains(browser)


# browser.quit()
'''

