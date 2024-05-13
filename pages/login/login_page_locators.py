from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_TXTBX = (By.ID, "customer_email")
    PASSWORD_TXTBX = (By.ID, "customer_password")
    LOGIN_BTN = (By.XPATH, '//*[@id="customer_login"]/div[3]/button')
