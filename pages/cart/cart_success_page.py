from pages.base_page import BasePage
from pages.cart.cart_success_page_locators import CartSuccessPageLocators


class CartSuccessPage(BasePage):

    def get_added_success_lbl(self):
        return self.find_element(CartSuccessPageLocators.ADD_SUCCESS_LBL).text

    def get_remove_success_lbl(self):
        return self.find_element(CartSuccessPageLocators.REMOVE_SUCCESS_LBL).text