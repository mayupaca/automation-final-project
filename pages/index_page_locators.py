from selenium.webdriver.common.by import By


class IndexPageLocators:
    ACCOUNT_LINK = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/i')
    LOGIN_LINK = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]')
    EMAIL_TXTBX = (By.ID, "input-email")
    PASSWORD_TXTBX = (By.ID, "input-password")
    LOGIN_BTN = (By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')

