from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By

class LoginPageLocators(BasePageLocators):
  LOGIN_LINK = (By.LINK_TEXT, 'Log in')
  DEVELOPER_LOGIN_BTN = (By.XPATH, '//a[@class="hr_button"]')
  LOGIN_TAB = (By.ID, 'tab-1-item-1')
  EMAIL_ADDRESS_FIELD = (By.XPATH, '//input[@name="username"]')
  PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
  REMEMBER_ME_CHECKBOX = (By.XPATH, '//input[@data-analytics="AuthPageRememberMe"]')
  LOGIN_BTN = (By.XPATH, '//span[text()="Log In"]')
  HACKERRANK_HOME_BTN = (By.XPATH, '//img[@alt="HackerRank Home"]')
  INVALID_CREDENTIALS_MESSAGE = (By.XPATH, '//span[text()="Invalid login or password. Please try again."]')
