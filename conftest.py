import pytest
from selenium import webdriver


def pytest_addoption(parser):
  parser.addoption("--browser_name", action="store", default="firefox")

@pytest.fixture(scope="class")
def setup_teardown(request):
  global driver
  browser_name = request.config.getoption("--browser_name")
  if(browser_name == "firefox"):
    driver = webdriver.Firefox()
  elif(browser_name == "chrome"):
    driver = webdriver.Chrome()
  driver.maximize_window()
  driver.implicitly_wait(5)
  request.cls.driver = driver
  yield
  # driver.close()
  driver.quit()