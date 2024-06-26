from pages.base_page import BasePage
from pages.login.login_success_page_locators import LoginSuccessPageLocators, LoginNotSuccessPageLocators
from resources.constans import MAX_WAIT_INTERVAL


class LoginSuccessPage(BasePage):

    def get_login_success_label(self):
        element = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginSuccessPageLocators.LOGIN_SUCCESS_LBL)
        return element.text

    def get_login_not_success_label(self):
        element = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginNotSuccessPageLocators.LOGIN_NOT_SUCCESS_LBL)
        return element.text

