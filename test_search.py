from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_google_search():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("https://www.google.com")
        # Находим поле поиска по имени (name="q")
        search_box = wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("pytest")
        search_box.submit()  # нажать Enter

        # Проверяем, что в заголовке страницы есть слово «pytest»
        wait.until(EC.title_contains("pytest"))
        assert "pytest" in driver.title
    finally:
        driver.quit()
