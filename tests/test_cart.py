import pytest
from pages.cart.cart_page import CartPage
from pages.cart.cart_success_page import CartSuccessPage
from resources.constans import TEST_SITE_URL
from pages.index_page import IndexPage
import time


@pytest.mark.usefixtures("driver")
class TestCart:

    def test_add_to_cart(self, driver):
        driver.get(TEST_SITE_URL)  # Adjust URL as needed
        cart_page = CartPage(driver)
        cart_page.click_add_to_cart()
        time.sleep(3)  # wait for cart update

        cart_success_page = CartSuccessPage(driver)
        assert "Item added to cart" == cart_success_page.get_success_message(), "Add to cart Test Failed"

        assert "1" == cart_page.get_cart_count(), "Cart count mismatch after adding item"

    def test_remove_from_cart(self, driver):
        driver.get(TEST_SITE_URL + "/cart-page")  # Adjust URL as needed
        cart_page = CartPage(driver)
        cart_page.click_remove_from_cart()
        time.sleep(3)  # wait for cart update

        cart_success_page = CartSuccessPage(driver)
        assert "Item removed from cart" == cart_success_page.get_success_message(), "Remove from cart Test Failed"

        assert "0" == cart_page.get_cart_count(), "Cart count mismatch after removing item"
