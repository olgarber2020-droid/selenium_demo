from selenium import webdriver
from selenium.webdriver.common.by import By

FORM_URL = "https://httpbin.qa-territory.online/forms/post"


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get(FORM_URL)

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Anna")

    submit_button = driver.find_element(
        By.XPATH, '//button[contains(., "Submit")]'
    )
    submit_button.click()

    assert driver.current_url != FORM_URL

    driver.quit()
