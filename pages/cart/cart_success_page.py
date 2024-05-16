from pages.base_page import BasePage
from pages.cart.cart_success_page_locators import CartSuccessPageLocators

class CartSuccessPage(BasePage):

    def get_success_message(self):
        return self.find_element(CartSuccessPageLocators.SUCCESS_MESSAGE).text