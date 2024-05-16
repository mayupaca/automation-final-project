from pages.base_page import BasePage
from pages.search.search_page_locators import SearchPageLocators
from resources.constans import MAX_WAIT_INTERVAL


class SearchPage(BasePage):

    def specific_item(self, specific_item):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SearchPageLocators.INPUT_BOX)
        self.find_element(SearchPageLocators.INPUT_BOX).send_keys(specific_item)
        self.find_element(SearchPageLocators.SELECTED_ITEM).click()

    def keyword_item(self, item_keyword):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SearchPageLocators.INPUT_BOX)
        self.find_element(SearchPageLocators.INPUT_BOX).send_keys(item_keyword)
        self.find_element(SearchPageLocators.SEARCH_BTN).click()
