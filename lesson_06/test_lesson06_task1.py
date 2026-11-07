from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    wait = WebDriverWait(driver, 10)
    start_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.example button")))
    start_btn.click()
    hello_text = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    driver.save_screenshot("hello_world.png")
    assert hello_text.text == "Hello World!"
    
    driver.quit()
