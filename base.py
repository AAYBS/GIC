from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """Base class to initialize the base page that will be called from pages"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, uri):
        url = self.base_url + uri

    def wait_for_visible(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))


class IssuesPage(BasePage):
    """Issues page action methods come here. in our e.g . Github/issues.com"""

    def __init__(self, driver):
        self.locators = IssuePageLocators
        super(IssuesPage, self).__init__(driver)

    def create_issue(self):
        self.find_element(*self.locators.ISSUE).click()
        self.wait_for_clickable(*self.locators.CLOSE_ISSUE).click()
        self.find_element(*self.locators.NEW_ISSUE).click()
        self.wait_for_visible(self.locators.TITLE).send_keys('Test')
        self.wait_for_visible(self.locators.DESCRIPTION).clear().send_keys('Test')
        self.find_element(*self.locators.LABELS).click()
        labels_list = self.wait_for_clickable(self.locators.LABELS_LIST)
        self.driver.execute_script("arguments[0].click();", labels_list)

class LoginPage(BasePage):
    """Login page action methods come here. in our e.g . Github/login.com"""

    def __init__(self, driver):
        self.locators = LoginPageLocators
        super(LoginPage, self).__init__(driver)

    def fill_sign_in(self):
        self.find_element(*self.locators.SIGN_IN).click()
        self.find_element(*self.locators.USER_NAME).send_keys('USER')
        self.find_element(*self.locators.PASSWORD).send_keys('PASS')
        self.find_element(*self.locators.COMMIT).click()