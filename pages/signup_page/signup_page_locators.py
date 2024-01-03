from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By

class SignupPageLocators(BasePageLocators):
  SIGNUP_TAB = (By.ID, 'tab-1-item-0')
  DEVELOPER_HEADER = (By.XPATH, '//h2[text()="For Developers"]')
  FULLNAME_FIELD = (By.ID, 'input-1')
  EMAIL_ADDRESS_FIELD = (By.ID, 'input-2')
  PASSWORD_FIELD = (By.ID, 'input-3')
  AGREE_CHECKBOX = (By.CLASS_NAME, 'checkbox-input')
  CREATE_AN_ACCOUNT_BTN = (By.XPATH, '//button[@data-analytics="SignupPassword"]')
  SIGNING_UP_BTN = (By.XPATH, '//span[text()="Signing up.."]')
  LEARN_COMPETE_BTN = (By.XPATH, '//span[text()="Learn & Compete with Others"]')
  SKIP_BTN = (By.XPATH, '//span[text()="Skip"]')
  NOT_NOW_BTN = (By.XPATH, '//span[text()="Not Now"]')