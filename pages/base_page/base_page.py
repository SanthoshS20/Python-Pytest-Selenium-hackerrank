from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import constants

class BasePage:

  def __init__(self, driver):
    self.driver = driver

  def click_webelement(self, locator):
    self.driver.find_element(*locator).click()

  def get_attribute_of_an_element(self, locator, attribute):
    return self.driver.find_element(*locator).get_attribute(attribute)

  def send_text(self, locator, text):
    self.driver.find_element(*locator).send_keys(text)

  def web_driver_wait(self, seconds):
    wait = WebDriverWait(self.driver, seconds)
    return wait

  def wait_until_element_should_be_visible(self, locator, seconds):
    self.wait = self.web_driver_wait(seconds)
    self.wait.until(expected_conditions.visibility_of_element_located(locator))

  def wait_until_element_should_not_be_visible(self, locator, seconds):
    self.wait = self.web_driver_wait(seconds)
    self.wait.until_not(expected_conditions.visibility_of_element_located((locator)))

  def get_element_text(self, locator):
    return self.driver.find_element(*locator).text

  def get_page_title(self):
    return self.driver.title

  def get_current_url(self):
    return self.driver.current_url

  def select_dropdown_option(self, locator, text):
    self.select = Select(self.driver.find_element(*locator))
    self.select.select_by_visible_text(text)

  def load_page(self):
    self.driver.get(constants.WEBSITE_URL)

  def check_element_is_enabled(self, locator):
    self.driver.find_element(*locator).is_enabled()

  def wait_until_element_should_be_enabled(self, locator, seconds):
    self.wait = self.web_driver_wait(seconds)
    self.wait.until(expected_conditions.element_to_be_clickable(locator))

  def click_element_by_js_code(self, element):
    self.driver.execute_script("arguments[0].click;", element)
