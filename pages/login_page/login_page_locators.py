from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By

class LoginPageLocators(BasePageLocators):
  LOGIN_LINK = (By.XPATH, '//div[@class="pagenav_dropdown--actions"]//child::a[text()="Log In"]')
  DEVELOPER_LOGIN_BTN = (By.XPATH, '//em[text()="Developers"]//parent::h2//parent::div//following-sibling::a')
  LOGIN_TAB = (By.ID, 'tab-1-item-1')
  EMAIL_ADDRESS_FIELD = (By.XPATH, '//input[@name="username"]')
  PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
  REMEMBER_ME_CHECKBOX = (By.XPATH, '//button[@id="remember-me"]')
  LOGIN_BTN = (By.XPATH, '//button[text()="Log In"]')
  HACKERRANK_HOME_BTN = (By.XPATH, '//img[@alt="HackerRank Home"]')
  INVALID_CREDENTIALS_MESSAGE = (By.XPATH, '//h3[text()="Invalid login or password. Please try again."]')
