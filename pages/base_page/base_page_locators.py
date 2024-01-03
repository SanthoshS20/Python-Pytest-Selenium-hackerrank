from selenium.webdriver.common.by import By

class BasePageLocators:
  SIGNUP_BTN = (By.LINK_TEXT, 'Sign up')
  DEVELOPER_BTN = (By.XPATH, '//a[@data-url="/signup"]')
  CREATE_ACCOUNT_BTN = (By.LINK_TEXT, 'Create account')
