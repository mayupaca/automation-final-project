from selenium.webdriver.common.by import By


class SearchPageLocators:
    INPUT_BOX = (By.XPATH, '//*[@id="shopify-section-static-header"]/div[1]/div[1]/div[2]/form/div[1]/input')
    SELECTED_ITEM = (By.XPATH, '//*[@id="shopify-section-static-header"]/div[1]/div[1]/div[2]/form/div[2]/div[2]/div[1]/a[1]')

    SEARCH_BTN = (By.XPATH, '//*[@id="shopify-section-static-header"]/div[1]/div[1]/div[2]/form/div[1]/button[2]')
