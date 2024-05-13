from pages.base_page import BasePage
from pages.login.login_page_locators import LoginPageLocators
from resources.constans import MAX_WAIT_INTERVAL


class LoginPage(BasePage):

    def login_user(self, user_name, password):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.EMAIL_TXTBX)
        self.find_element(LoginPageLocators.EMAIL_TXTBX).send_keys(user_name)
        self.find_element(LoginPageLocators.PASSWORD_TXTBX).send_keys(password)
        self.find_element(LoginPageLocators.LOGIN_BTN).click()
