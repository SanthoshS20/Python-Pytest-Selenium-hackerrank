from pages.base_page.base_page import BasePage
from pages.login_page.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

  def __init__(self, driver):
    self.driver = driver
    super().__init__(driver)

  def click_login_link(self):
    self.click_webelement(LoginPageLocators.LOGIN_LINK)
    self.wait_until_element_should_be_visible(LoginPageLocators.DEVELOPER_LOGIN_BTN, 10)

  def click_developer_login_button(self):
    self.click_webelement(LoginPageLocators.DEVELOPER_LOGIN_BTN)
    self.wait_until_element_should_be_visible(LoginPageLocators.LOGIN_TAB, 10)
    self.wait_until_element_should_be_visible(LoginPageLocators.LOGIN_BTN, 10)

  def click_login_tab(self):
    self.click_webelement(LoginPageLocators.LOGIN_TAB)
    self.wait_until_element_should_be_visible(LoginPageLocators.LOGIN_BTN, 10)

  def fill_email_address(self, email_address):
    self.send_text(LoginPageLocators.EMAIL_ADDRESS_FIELD, email_address)

  def get_email_address_attribute_value(self):
    return self.get_attribute_of_an_element(LoginPageLocators.EMAIL_ADDRESS_FIELD, "value")

  def fill_password(self, password):
    self.send_text(LoginPageLocators.PASSWORD_FIELD, password)

  def get_password_attribute_value(self):
    return self.get_attribute_of_an_element(LoginPageLocators.PASSWORD_FIELD, "value")

  def click_login_button(self):
    self.click_webelement(LoginPageLocators.LOGIN_BTN)

  def check_home_button_visibility(self):
    self.wait_until_element_should_be_visible(LoginPageLocators.HACKERRANK_HOME_BTN, 10)

  def check_invalid_credentials_error_message(self):
    self.wait_until_element_should_be_visible(LoginPageLocators.INVALID_CREDENTIALS_MESSAGE, 10)

  def check_remember_me_checkbox(self):
    self.click_webelement(LoginPageLocators.REMEMBER_ME_CHECKBOX)

