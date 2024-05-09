from selenium.webdriver.common.by import By


class LoginSuccessPageLocators:
    LOGIN_SUCCESS_LBL = (By.XPATH, '//*[@id="content"]/h2[1]')


class LoginNotSuccessPageLocators:
    LOGIN_NOT_SUCCESS_LBL = (By.XPATH, '//*[@id="account-login"]/div[1]')


