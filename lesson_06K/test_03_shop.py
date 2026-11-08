from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"
ITEMS = [
    "add-to-cart-sauce-labs-backpack",
    "add-to-cart-sauce-labs-bolt-t-shirt",
    "add-to-cart-sauce-labs-onesie",
]
EXPECTED_TOTAL = "Total: $58.29"


def test_shop_total():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(URL)

        wait.until(EC.visibility_of_element_located(
            (By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        for item_id in ITEMS:
            wait.until(EC.element_to_be_clickable(
                (By.ID, item_id))).click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        wait.until(EC.visibility_of_element_located(
            (By.ID, "first-name"))).send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        total_text = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label"))).text
    finally:
        driver.quit()

    assert total_text == EXPECTED_TOTAL
