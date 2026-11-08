from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

FIELDS = {
    "first-name": "Ольга",
    "last-name": "Гарбер",
    "address": "Еремеева, 1-31",
    "e-mail": "olik75@yandex.ru",
    "phone": "+79821000903",
    "zip-code": "",
    "city": "Аша",
    "country": "Россия",
    "job-position": "QA",
    "company": "SkyPro",
}

EXPECTED_VALUES = [
    "Ольга", "Гарбер", "Еремеева, 1-31", "olik75@yandex.ru",
    "+79821000903", "Аша", "Россия", "QA", "SkyPro",
]

COLLECT_SCRIPT = r"""
const items = [];
for (const el of document.querySelectorAll('*')) {
    const s = getComputedStyle(el);
    const colors = [s.backgroundColor, s.borderTopColor];
    let kind = null;
    for (const c of colors) {
        const m = c.match(
            /rgba?\$(\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\$/);
        if (!m) continue;
        if (m[4] !== undefined && parseFloat(m[4]) === 0) continue;
        const r = +m[1], g = +m[2], b = +m[3];
        if (g > r + 10 && g > b - 20) kind = kind || 'green';
        if (r > g + 25 && r > b - 20) kind = kind || 'red';
    }
    if (!kind) continue;
    let text = (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA')
        ? el.value : (el.textContent || '').trim();
    text = text.slice(0, 60);
    if (!text) continue;
    items.push({kind: kind, text: text, cls: el.className.slice(0, 60)});
}
return items;
"""


def make_driver():
    options = webdriver.EdgeOptions()
    options.add_experimental_option("prefs", {
        "autofill.profile_enabled": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    })
    return webdriver.Edge(options=options)


def test_form_validation():
    driver = make_driver()
    wait = WebDriverWait(driver, 15)
    try:
        driver.get(URL)
        driver.maximize_window()
        wait.until(EC.presence_of_element_located(
            (By.NAME, "first-name")))

        for name, value in FIELDS.items():
            field = wait.until(
                EC.presence_of_element_located((By.NAME, name)))
            field.clear()
            if value:
                field.send_keys(value)

        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type=submit]")))
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", submit)
        try:
            submit.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", submit)

        # Ждём, пока страница перезагрузится
        wait.until(lambda d: "submitted" in d.current_url)

        # Проверяем, что поле Zip code стало красным
        zip_code = wait.until(
            EC.presence_of_element_located((By.ID, "zip-code"))
        )
        assert "alert-danger" in zip_code.get_attribute("class"), \
            f"Поле Zip code не красное! " \
            f"Классы: {zip_code.get_attribute('class')}"

        # Список полей, которые должны стать зелеными
        green_fields = [
            "first-name", "last-name", "address", "city",
            "country", "e-mail", "phone", "job-position", "company"
        ]

        for field_id in green_fields:
            # Ждём появления поля
            field = wait.until(
                EC.presence_of_element_located((By.ID, field_id)))
            assert "alert-success" in field.get_attribute("class"), \
                f"Поле {field_id} не зелёное! " \
                f"Классы: {field.get_attribute('class')}"

    finally:
        driver.quit()
