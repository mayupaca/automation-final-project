from selenium.webdriver.common.by import By


class CartPageLocators:
    ITEM = (By.XPATH, '//*[@id="shopify-section-template--16887881236668__main"]/div[2]/div[1]/ul/li[1]/div/div/div[1]/a/figure/img[1]')
    ADD_CART_BTN = (By.XPATH, '//*[@id="product_form_8323275063484"]/div/button/span[1]')
    QUANTITY_UP = (By.XPATH, '//*[@id="product_form_8323275063484"]/div/div[1]/div/button[2]')
    QUANTITY_DOWN = (By.XPATH, '//*[@id="product_form_8323275063484"]/div/div[1]/div/button[2]')
    CART_BTN = (By.ID, 'site-header-cart__count')
    RETURN_TO_CART_BTN = (By.XPATH, '//*[@id="cart-page-popup-rec"]/div[2]/a')
    CLOSE_BTN = (By.ID, 'Capa_1')

