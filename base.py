from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser

class BasePage(object):
    """Base class to initialize the base page that will be called from pages"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def close(self):
        self.driver.quit()

    def wait_for_visible(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))


class IssuesPage(BasePage):
    """Issues page action methods come here. in our e.g . Github/issues.com"""

    def __init__(self, driver):
        self.locators = IssuePageLocators
        super(IssuesPage, self).__init__(driver)
        self.title_text = self.config.get('ISSUES', 'TITLE')
        self.description_text = self.config.get('ISSUES', 'DESCRIPTION')
        self.labels = self.config.get('ISSUES', 'LABELS').split(",")

    def create_issue(self):
        self.find_element(*self.locators.NEW_ISSUE).click()
        self.wait_for_visible(self.locators.TITLE).send_keys(self.title_text)
        self.wait_for_visible(self.locators.DESCRIPTION)\
            .send_keys(self.description_text)
        self.set_labels(self.labels)
        self.wait_for_visible(self.locators.SUBMIT).click()

    def set_labels(self, labels):
        self.wait_for_visible(self.locators.LABELS).click()
        for label in labels:

            # A locator for the specific label option we're interested in
            label_locator = list(self.locators.LABELS_OPTION)
            label_locator[1] = label_locator[1].format(label_name=label)

            self.wait_for_visible(label_locator).click()
        self.wait_for_visible(self.locators.LABELS).click()

class LoginPage(BasePage):
    """Login page action methods come here. in our e.g . Github/login.com"""

    def __init__(self, driver):
        self.locators = LoginPageLocators
        super(LoginPage, self).__init__(driver)
        self.user_name = self.config.get('LOGIN', 'USER_NAME')
        self.password = self.config.get('LOGIN', 'PASSWORD')

    def fill_sign_in(self):
        self.find_element(*self.locators.SIGN_IN).click()
        self.find_element(*self.locators.USER_NAME).send_keys(self.user_name)
        self.find_element(*self.locators.PASSWORD).send_keys(self.password)
        self.find_element(*self.locators.COMMIT).click()
