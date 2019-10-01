from selenium.webdriver.common.by import By


# separate each page in different locator
class LoginPageLocators(object):
    USER_NAME = (By.ID, 'login_field')
    PASSWORD = (By.ID, 'password')
    SIGN_IN = (By.LINK_TEXT, 'Sign in')
    COMMIT = (By.NAME, 'commit')


class IssuePageLocators(object):
    ISSUE = (By.LINK_TEXT, 'Add new algorithm, data structure, puzzle, cipher')
    CLOSE_ISSUE = (By.NAME, 'comment_and_close')
    NEW_ISSUE = (By.LINK_TEXT, 'New issue')
    TITLE = (By.ID, 'issue_title')
    DESCRIPTION = (By.ID, 'issue_body')
    LABELS = (By.ID, 'labels-select-menu')
    LABELS_OPTION = (By.XPATH, "//div[@class='select-menu-item-text']//span[@class='name' and contains(., '{label_name}')]")
    SUBMIT = (By.XPATH, "//button[@type='submit' and contains(., 'Submit new issue')]")
