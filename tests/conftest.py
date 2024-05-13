import pytest as pytest
from selenium import webdriver
import config


@pytest.fixture(scope="function")
def username_password():
    user_name = config.USER_NAME
    password = config.USER_PASSWORD

    return [user_name, password]


@pytest.fixture(scope="function")
def wrong_username_password():
    user_name = "hogehoge@gmail.com"
    password = "1234567"

    return [user_name, password]


@pytest.fixture(scope="class")
def driver():
    _driver = webdriver.Chrome()
    _driver.implicitly_wait(5)
    yield _driver
    _driver.quit()
