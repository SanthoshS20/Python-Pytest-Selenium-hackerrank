from pages.signup_page.signup_page import SignupPage
from utils.utilities import Utilities
import pytest, logging, constants, time

@pytest.mark.usefixtures("setup_teardown")
class TestSignupPage:

  def setup_method(self, method):
    self.utils = Utilities(__name__, logging.DEBUG)
    self.logs = self.utils.get_logger()
    self.signup_page = SignupPage(self.driver)
    self.logs.debug("Created Signup Page Instance.")
    self.signup_page.load_page()
    self.logs.info("Page loaded.")

  def test_create_account_with_valid_credentials(self):
    self.signup_page.click_signup_button()
    self.signup_page.click_developer_button()
    self.signup_page.click_create_account_button()
    self.signup_page.fill_fullname_field(constants.FIRST_NAME, constants.LAST_NAME)
    self.signup_page.fill_email_address_field(constants.EMAIL_ADDRESS)
    self.signup_page.fill_password_field(constants.PASSWORD)
    self.signup_page.click_agree_checkbox()
    assert constants.FIRST_NAME + " " + constants.LAST_NAME == self.signup_page.get_fullname_field_value(), f"Fullname field doesn't have {constants.FIRST_NAME} {constants.LAST_NAME}"
    assert constants.EMAIL_ADDRESS == self.signup_page.get_email_address_field_value(), f"Email address field doesn't have {constants.EMAI}"
    assert constants.PASSWORD == self.signup_page.get_password_field_value(), f"Password field doesn't have {constants.PASSWORD}"
    self.signup_page.click_create_an_account_button()
    # time.sleep(10)
    self.signup_page.click_learn_compete_button()
    self.signup_page.click_skip_button()
    self.signup_page.click_not_now_button()
    assert self.signup_page.get_current_url() == constants.DASHBOARD_URL, f"Incorrect URL"
