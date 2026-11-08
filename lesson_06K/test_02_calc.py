from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"


def test_slow_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 60)
    try:
        driver.get(URL)
        driver.maximize_window()

        delay_input = wait.until(
            EC.presence_of_element_located((By.ID, "delay")))
        delay_input.clear()
        delay_input.send_keys("45")

        for key in ["7", "+", "8", "="]:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//span[text()='{key}']"))).click()

        wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), "15"))

        screen = driver.find_element(By.CLASS_NAME, "screen")
        print(f"На экране калькулятора: {screen.text!r}")
        assert screen.text.strip() == "15"
    finally:
        driver.quit()
