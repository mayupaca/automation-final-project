from selenium.webdriver.common.by import By


class SearchPageLocators:
    INPUT_BOX = (By.XPATH, '//*[@id="shopify-section-static-header"]/div[1]/div[1]/div[2]/form/div[1]/input')
    SEARCH_BTN = (By.XPATH, '//*[@id="shopify-section-static-header"]/div[1]/div[1]/div[2]/form/div[1]/button[2]')
