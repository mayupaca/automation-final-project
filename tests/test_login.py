import pytest
from pages.login.login_page import LoginPage
from pages.login.login_success_page import LoginSuccessPage
from resources.constans import TEST_SITE_URL
from pages.index_page import IndexPage
import logging
import time

logging.basicConfig(level=logging.INFO)


@pytest.mark.usefixtures("driver")
class TestLogin:

    def test_wrong_login(self, driver, wrong_username_password):
        logging.info("Starting test_wrong_login")
        login_page = LoginPage(driver)
        login_page.navigate_to(TEST_SITE_URL)
        time.sleep(3)

        index_page = IndexPage(driver)
        index_page.click_on_decline_offer_btn()
        time.sleep(2)
        index_page.click_on_decline_offer_btn()
        time.sleep(2)

        index_page.click_on_login_btn()
        time.sleep(2)

        login_page.login_user(wrong_username_password[0], wrong_username_password[1])
        time.sleep(3)

        login_not_success_page = LoginSuccessPage(driver)
        login_not_success_lbl = login_not_success_page.get_login_not_success_label()
        assert "Incorrect email or password." == login_not_success_lbl, "Login Test Case 1 Failed"
        time.sleep(3)

    def test_correct_login(self, driver, username_password):
        logging.info("Starting test_correct_login")
        login_page = LoginPage(driver)
        login_page.navigate_to(TEST_SITE_URL)
        time.sleep(3)

        index_page = IndexPage(driver)
        index_page.click_on_login_btn()
        time.sleep(2)

        login_page.login_user(username_password[0], username_password[1])
        time.sleep(3)

        login_success_page = LoginSuccessPage(driver)
        login_success_lbl = login_success_page.get_login_success_label()
        assert "My Account" == login_success_lbl, "Login Test Case 2 Failed"
        time.sleep(10)
