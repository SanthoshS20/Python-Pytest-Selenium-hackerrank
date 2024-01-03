from pages.base_page.base_page import BasePage
from pages.signup_page.signup_page_locators import SignupPageLocators

class SignupPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver

  def click_signup_button(self):
    self.click_webelement(SignupPageLocators.SIGNUP_BTN)
    self.wait_until_element_should_be_visible(SignupPageLocators.DEVELOPER_BTN, 10)

  def click_developer_button(self):
    self.click_webelement(SignupPageLocators.DEVELOPER_BTN)
    self.wait_until_element_should_be_enabled(SignupPageLocators.CREATE_ACCOUNT_BTN, 10)

  def click_signup_tab(self):
    self.click_webelement(SignupPageLocators.SIGNUP_TAB)
    self.wait_until_element_should_be_visible(SignupPageLocators.SIGNUP_BTN, 10)

  def fill_fullname_field(self, firstname, lastname):
    self.send_text(SignupPageLocators.FULLNAME_FIELD, firstname + " " + lastname)

  def fill_email_address_field(self, email_address):
    self.send_text(SignupPageLocators.EMAIL_ADDRESS_FIELD, email_address)

  def fill_password_field(self, password):
    self.send_text(SignupPageLocators.PASSWORD_FIELD, password)

  def click_create_account_button(self):
    self.click_webelement(SignupPageLocators.CREATE_ACCOUNT_BTN)
    self.wait_until_element_should_be_visible(SignupPageLocators.DEVELOPER_HEADER, 10)
    self.wait_until_element_should_be_visible(SignupPageLocators.SIGNUP_TAB, 10)

  def click_agree_checkbox(self):
    self.click_webelement(SignupPageLocators.AGREE_CHECKBOX)

  def click_create_an_account_button(self):
    self.click_webelement(SignupPageLocators.CREATE_AN_ACCOUNT_BTN)
    self.wait_until_element_should_not_be_visible(SignupPageLocators.SIGNING_UP_BTN, 10)
    self.wait_until_element_should_be_visible(SignupPageLocators.LEARN_COMPETE_BTN, 10)

  def click_learn_compete_button(self):
    self.wait_until_element_should_be_enabled(SignupPageLocators.LEARN_COMPETE_BTN, 10)
    self.click_webelement(SignupPageLocators.LEARN_COMPETE_BTN)
    self.wait_until_element_should_be_visible(SignupPageLocators.SKIP_BTN, 10)

  def click_skip_button(self):
    self.click_webelement(SignupPageLocators.SKIP_BTN)
    self.wait_until_element_should_be_visible(SignupPageLocators.NOT_NOW_BTN, 10)

  def click_not_now_button(self):
    self.click_webelement(SignupPageLocators.NOT_NOW_BTN)
    self.wait_until_element_should_not_be_visible(SignupPageLocators.NOT_NOW_BTN, 10)
    
  def get_fullname_field_value(self):
    return self.get_attribute_of_an_element(SignupPageLocators.FULLNAME_FIELD, "value")
  
  def get_email_address_field_value(self):
    return self.get_attribute_of_an_element(SignupPageLocators.EMAIL_ADDRESS_FIELD, "value")
  
  def get_password_field_value(self):
    return self.get_attribute_of_an_element(SignupPageLocators.PASSWORD_FIELD, 'value')
  
  