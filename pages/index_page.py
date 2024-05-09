from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constans import MAX_WAIT_INTERVAL


class IndexPage(BasePage):

    def click_on_account_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.ACCOUNT_LINK).click()

    def click_on_login_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.LOGIN_LINK).click()

