from selenium.webdriver.common.by import By


class CartPageLocators:
    SELECTED_ITEM = (By.XPATH, '//*[@id="shopify-section-template--16906041098428__main"]/div[2]/div[1]/ul/li[2]/div/div/div[1]')
    ADD_CART_BTN = (By.XPATH, '//*[@id="product_form_7727762145468"]/div[2]/button/span[1]')
    QUANTITY_UP = (By.XPATH, '//*[@id="product_form_7727762145468"]/div[2]/div[1]/div/button[2]')
    QUANTITY_DOWN = (By.XPATH, '//*[@id="product_form_7727762145468"]/div[2]/div[1]/div/button[1]')
    CART_BTN = (By.ID, 'site-header-cart__count')
    RETURN_TO_CART_BTN = (By.XPATH, '//*[@id="cart-page-popup-rec"]/div[2]/a')
    CLOSE_BTN = (By.ID, 'Capa_1')
    REMOVE_ITEM_BTN = (By.XPATH, '//*[@id="shopify-section-template--16906036773052__main"]/form/section/div/ul/li[1]/div/div[2]/div[3]/a')

# //*[@id="shopify-section-template--16906036773052__main"]/form/section/div/ul/li[1]/div/div[2]/div[3]/a/svg/path
# //*[@id="shopify-section-template--16906036773052__main"]/form/section/div/ul/li[1]/div/div[2]/div[3]/a/svg/path

#//*[@id="shopify-section-template--16906036773052__main"]/form/section/div/ul/li/div/div[2]/div[3]/a/svg/path