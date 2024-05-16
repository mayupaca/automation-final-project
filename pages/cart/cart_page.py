from pages.base_page import BasePage
from pages.cart.cart_page_locators import CartPageLocators
from resources.constans import MAX_WAIT_INTERVAL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CartPage(BasePage):

    def add_to_cart(self):
        self.find_element(CartPageLocators.SELECTED_ITEM).click()
        self.find_element(CartPageLocators.ADD_CART_BTN).click()
        self.find_element(CartPageLocators.CART_BTN).click()

    def remove_from_cart(self):
        # ポップアップが存在する場合のみ処理を実行
        try:
            return_to_cart_btn = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(
                EC.visibility_of_element_located(CartPageLocators.RETURN_TO_CART_BTN)
            )
            return_to_cart_btn.click()  # ポップアップが見つかった場合にのみクリック
            self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CartPageLocators.REMOVE_ITEM_BTN)
            self.find_element(CartPageLocators.REMOVE_ITEM_BTN).click()
        except TimeoutException:
            print("No popup was found.")  # ポップアップが見つからなかった場合の処理

    def get_cart_count(self):
        return self.find_element(CartPageLocators.CART_COUNT).text
