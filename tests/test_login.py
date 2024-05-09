from pages.login.login_page import LoginPage
from pages.login.login_success_page import LoginSuccessPage
from resources.constans import TEST_SITE_URL
from pages.index_page import IndexPage


class TestLogin:

    # Test Case wrong user login
    def test_wrong_login(self, driver, wrong_username_password):
        login_page = LoginPage(driver)
        login_page.navigate_to(TEST_SITE_URL)
        index_page = IndexPage(driver)
        index_page.click_on_account_btn()
        index_page.click_on_login_btn()
        login_page.login_user(wrong_username_password[0], wrong_username_password[1])
        login_success_page = LoginSuccessPage(driver)
        login_success_lbl = login_success_page.get_login_success_label()
        assert "Warning: No match for E-Mail Address and/or Password." == login_success_lbl, "Test Case 1 Failed"

    # Test Case correct user login
    def test_correct_login(self, driver, username_password):
        login_page = LoginPage(driver)
        login_page.navigate_to(TEST_SITE_URL)
        index_page = IndexPage(driver)
        index_page.click_on_account_btn()
        index_page.click_on_login_btn()
        login_page.login_user(username_password[0], username_password[1])
        login_success_page = LoginSuccessPage(driver)
        login_success_lbl = login_success_page.get_login_success_label()
        assert "My Account" == login_success_lbl, "Test Case 2 Failed"

