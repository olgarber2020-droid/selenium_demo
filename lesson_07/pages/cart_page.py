from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object страницы корзины."""

    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")

    def get_items_count(self):
        """Возвращает количество товаров в корзине."""
        self.wait_for(self.CART_ITEMS)
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def click_checkout(self):
        self.wait_for_clickable(self.CHECKOUT_BUTTON).click()
