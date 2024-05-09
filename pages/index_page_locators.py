from selenium.webdriver.common.by import By


class IndexPageLocators:
    HEJ_lINK = (By.ID, "hnf-header-profile")
    SIGNIN_LINK = (By.ID, "header__button")
    USER_NAME_TXTBX = (By.ID, "username")
    PASSWORD_TXTBX = (By.ID, "password")
    CONTINUE_BTN = (By.ID, "submitButton")

