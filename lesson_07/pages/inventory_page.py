from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object главной страницы магазина (каталог товаров)."""

    ADD_TO_CART_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'inventory_item')][.//div[text()='{name}']]"
        "//button[contains(@class, 'btn_inventory')]",
    )
    CART_LINK = (By.CSS_SELECTOR, "#shopping_cart_container a")

    def add_to_cart(self, product_name):
        """Добавляет товар в корзину по его названию."""
        button = self.wait_for_clickable(
            (self.ADD_TO_CART_BUTTON[0],
             self.ADD_TO_CART_BUTTON[1].format(name=product_name))
        )
        button.click()

    def go_to_cart(self):
        self.wait_for_clickable(self.CART_LINK).click()
