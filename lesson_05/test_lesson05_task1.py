from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "https://httpbin.qa-territory.online"


def test_navigation():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    assert driver.current_url.rstrip("/") == BASE_URL

    link = driver.find_element(By.LINK_TEXT, "HTML Form")
    link.click()
    assert "/forms/post" in driver.current_url

    driver.back()
    assert driver.current_url.rstrip("/") == BASE_URL

    driver.quit()
