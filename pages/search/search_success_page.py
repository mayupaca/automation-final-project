from pages.base_page import BasePage
from pages.search.search_success_page_locators import SpecificISuccessPageLocators, KeywordISuccessPageLocators
from resources.constans import MAX_WAIT_INTERVAL


class SearchSuccessPage(BasePage):

    def get_specific_i_success_label(self):
        element = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SpecificISuccessPageLocators.SPECIFIC_I_SUCCESS_LBL)
        return element.text

    def get_keyword_i_success_label(self):
        element = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, KeywordISuccessPageLocators.KEYWORD_I_SUCCESS_LBL)
        return element.text

# Search results for “bag” (101)