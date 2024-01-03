from pages.login_page.login_page import LoginPage
from utils.utilities import Utilities
import constants, logging, pytest


@pytest.mark.usefixtures("setup_teardown")
class TestLoginPage:

  def setup_method(self, method):
    self.login = LoginPage(self.driver)
    self.utils = Utilities(__name__, logging.DEBUG)
    self.logs = self.utils.get_logger()
    self.driver.delete_all_cookies()
    self.login.load_page()
    self.logs.debug("Page load successfully.")


  @pytest.mark.login
  def test_login_with_valid_credentials(self):
    self.login.click_login_link()
    self.logs.info("Clicked login link.")
    self.login.click_developer_login_button()
    self.logs.info("CLicked developer login button.")
    self.login.click_login_tab()
    self.logs.info("CLicked Login Tab.")
    self.login.fill_email_address(constants.EMAIL_ADDRESS)
    self.logs.debug(f"Filled email address field with {constants.EMAIL_ADDRESS}")
    self.login.fill_password(constants.PASSWORD)
    self.logs.debug(f"Password field with {constants.PASSWORD}")
    assert constants.EMAIL_ADDRESS == self.login.get_email_address_attribute_value(), f"Email address field doesn't hold {constants.EMAIL_ADDRESS}"
    assert constants.PASSWORD == self.login.get_password_attribute_value(), f"Password field doesn't hold {constants.PASSWORD}"
    self.login.click_login_button()
    self.logs.info("CLicked login button.")
    self.login.check_home_button_visibility()
    assert self.login.get_current_url() == constants.DASHBOARD_URL
    self.logs.info("Asserted dashboard URL.")

  @pytest.mark.login
  def test_login_with_invalid_credentials(self):
    self.login.click_login_link()
    self.logs.info("CLicked login link.")
    self.login.click_developer_login_button()
    self.logs.info("Clicked developer login button.")
    self.login.click_login_tab()
    self.logs.info("CLicked login tab")
    self.login.fill_email_address(constants.EMAIL_ADDRESS)
    self.logs.debug(f"Filled Email address with {constants.EMAIL_ADDRESS}")
    self.login.fill_password(constants.INCORRECT_PASSWORD)
    self.logs.debug(f"Filled Password with {constants.INCORRECT_PASSWORD}")
    assert constants.EMAIL_ADDRESS == self.login.get_email_address_attribute_value(), f"Email address field doesn't have {constants.EMAIL_ADDRESS}"
    assert constants.INCORRECT_PASSWORD == self.login.get_password_attribute_value(), f"Password field doesn't have {constants.INCORRECT_PASSWORD}"
    self.login.check_remember_me_checkbox()
    self.logs.info("Checked remember me checkbox.")
    self.login.click_login_button()
    self.logs.info("CLicked login button.")
    self.login.check_invalid_credentials_error_message()
    self.logs.warning("Invalid Credentials Message.")

