from selenium.webdriver.common.by import By

class IndexPageLocators:
    LOGIN_LINK = (By.XPATH, '//*[@id="site-header-nav"]/nav/ul[2]/li[2]')
    EMAIL_TXTBX = (By.ID, "customer_email")
    PASSWORD_TXTBX = (By.ID, "customer_password")
    LOGIN_BTN = (By.XPATH, '//*[@id="customer_login"]/div[3]/button')
    CLOSE_OFFER_BTN = (By.ID, 'bx-close-inside-2559033')
    DECLINE_OFFER_BTN = (By.ID, 'bx-element-2559033-yKwVZjN')

