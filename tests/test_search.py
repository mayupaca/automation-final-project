import pytest
from pages.login.login_page import LoginPage
from resources.constans import TEST_SITE_URL
from pages.index_page import IndexPage
from pages.search.search_page import SearchPage
from pages.search.search_success_page import SearchSuccessPage
import time


@pytest.mark.usefixtures("driver")
class TestSearch:
    def test_search_specific_i(self, driver, search_item, username_password):
        login_page = LoginPage(driver)
        login_page.navigate_to(TEST_SITE_URL)
        time.sleep(3)

        index_page = IndexPage(driver)
        index_page.click_on_decline_offer_btn()
        time.sleep(2)
        index_page.click_on_decline_offer_btn()
        time.sleep(2)

        index_page.click_on_login_btn()
        time.sleep(2)

        login_page.login_user(username_password[0], username_password[1])
        time.sleep(3)

        # Start search
        search_page = SearchPage(driver)

        search_page.specific_item(search_item[0])
        time.sleep(3)

        specific_i_success_page = SearchSuccessPage(driver)
        specific_i_success_lbl = specific_i_success_page.get_specific_i_success_label()
        assert "Search results for “dango mini jute bag” (19)" == specific_i_success_lbl, "Search Test Case 1 Failed"
        time.sleep(3)


