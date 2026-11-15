import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

ITEMS = [
    "Sauce Labs Backpack",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Onesie",
]


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


def test_purchase_flow(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory = InventoryPage(driver)
    for item in ITEMS:
        inventory.add_to_cart(item)
    inventory.go_to_cart()

    cart = CartPage(driver)
    assert cart.get_items_count() == len(ITEMS)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_form("Иван", "Иванов", "454000")
    checkout.click_continue()

    total = checkout.get_total()
    assert total == "Total: $58.29"
