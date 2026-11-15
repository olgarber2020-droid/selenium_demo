import pytest
from selenium import webdriver


@pytest.fixture
def chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def firefox():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()
