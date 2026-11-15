from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page Object страниц оформления заказа (форма и сводка заказа)."""

    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    ZIP_CODE = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")
    TOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_form(self, first_name, last_name, zip_code):
        self.wait_for(self.FIRST_NAME).send_keys(first_name)
        self.wait_for(self.LAST_NAME).send_keys(last_name)
        self.wait_for(self.ZIP_CODE).send_keys(zip_code)

    def click_continue(self):
        self.wait_for_clickable(self.CONTINUE_BUTTON).click()

    def get_total(self):
        """Читает итоговую стоимость со страницы сводки заказа."""
        return self.wait_for(self.TOTAL).text
