from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constans import MAX_WAIT_INTERVAL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IndexPage(BasePage):

    def click_on_login_btn(self):
        WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(
            EC.element_to_be_clickable(IndexPageLocators.LOGIN_LINK)
        ).click()

    def click_on_close_offer_btn(self):
        WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(
            EC.element_to_be_clickable(IndexPageLocators.CLOSE_OFFER_BTN)
        ).click()

    def click_on_decline_offer_btn(self):
        WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(
            EC.element_to_be_clickable(IndexPageLocators.DECLINE_OFFER_BTN)
        ).click()


