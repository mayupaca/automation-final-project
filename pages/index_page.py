from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constans import MAX_WAIT_INTERVAL


class IndexPage(BasePage):

    def click_on_hej_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.HEJ_lINK)

    def click_on_signin_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.SIGNIN_LINK)

