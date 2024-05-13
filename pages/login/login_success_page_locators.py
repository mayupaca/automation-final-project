from selenium.webdriver.common.by import By


class LoginSuccessPageLocators:
    LOGIN_SUCCESS_LBL = (By.XPATH, '//*[@id="site-main"]/section/header/h1')


class LoginNotSuccessPageLocators:
    LOGIN_NOT_SUCCESS_LBL = (By.XPATH, '//*[@id="customer_login"]/div[1]/div/ul/li')


