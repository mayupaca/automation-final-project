import pytest
from resources.constans import TEST_SITE_URL
from pages.login.login_page import LoginPage
from pages.index_page import IndexPage
from pages.search.search_page import SearchPage
from pages.cart.cart_page import CartPage
from pages.cart.cart_success_page import CartSuccessPage
import time


@pytest.mark.usefixtures("driver")
class TestCart:

    def test_add_to_cart(self, driver, search_item, username_password):
        login_page = LoginPage(driver)
        login_page.navigate_to(TEST_SITE_URL)
        time.sleep(3)

        index_page = IndexPage(driver)
        index_page.click_on_decline_offer_btn()
        time.sleep(2)
        index_page.click_on_decline_offer_btn()
        time.sleep(2)

        index_page.click_on_login_btn()

        login_page.login_user(username_password[0], username_password[1])
        time.sleep(3)

        # Start search
        search_page = SearchPage(driver)
        search_page.keyword_item(search_item[1])
        time.sleep(3)

        # Add cart
        cart_page = CartPage(driver)
        cart_page.add_to_cart()

        cart_success_page = CartSuccessPage(driver)
        assert "Your cart" == cart_success_page.get_added_success_lbl(), "Add to cart Test Failed"

    def test_remove_from_cart(self, driver):
        cart_page = CartPage(driver)
        cart_page.remove_from_cart()
        time.sleep(3)

        cart_success_page = CartSuccessPage(driver)
        assert "Your cart" == cart_success_page.get_remove_success_lbl(), "Remove from cart Test Failed"

        # assert "0" == cart_page.get_cart_count(), "Cart count mismatch after removing item"
