from pages.base_page import BasePage
from pages.cart.cart_page_locators import CartPageLocators


class CartPage(BasePage):

    def click_add_to_cart(self):
        self.find_element(CartPageLocators.ADD_TO_CART_BTN).click()

    def click_remove_from_cart(self):
        self.find_element(CartPageLocators.REMOVE_FROM_CART_BTN).click()

    def get_cart_count(self):
        return self.find_element(CartPageLocators.CART_COUNT).text
