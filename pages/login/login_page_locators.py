from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_TXTBX = (By.ID, "input-email")
    PASSWORD_TXTBX = (By.ID, "input-password")
    LOGIN_BTN = (By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')

