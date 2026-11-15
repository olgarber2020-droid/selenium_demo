import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    calc = CalculatorPage(driver)
    calc.open()
    calc.set_delay(45)
    for label in ("7", "+", "8", "="):
        calc.click_button(label)

    result = calc.wait_for_result("15", timeout=50)
    assert result == "15"
