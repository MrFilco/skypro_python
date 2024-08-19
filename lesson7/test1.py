import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()

def wait_for_element(driver, by, value, timeout=40):
    """Ожидание видимости элемента на странице."""
    try:
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
    except Exception as e:
        driver.save_screenshot(f'error_{value}.png')
        raise AssertionError(f"Ошибка при ожидании элемента '{value}'. Exception: {e}")

def fill_form_fields(driver, fields):
    """Заполнение полей формы данными."""
    for field_name, value in fields.items():
        print(f"Заполняем поле: {field_name}")
        field = wait_for_element(driver, By.NAME, field_name)
        field.send_keys(value)

def validate_field_success(driver, field_name):
    """Проверка успешного заполнения поля (подсветка зеленым)."""
    field = wait_for_element(driver, By.ID, field_name)
    if "alert-success" not in field.get_attribute("class").split():
        driver.save_screenshot(f'validation_error_{field_name}.png')
    assert "alert-success" in field.get_attribute("class").split(), f"Поле '{field_name}' должно быть подсвечено зеленым."

def validate_field_error(driver, field_id):
    """Проверка ошибки в поле (подсветка красным)."""
    field = wait_for_element(driver, By.ID, field_id)
    if "alert-danger" not in field.get_attribute("class").split():
        driver.save_screenshot(f'validation_error_{field_id}.png')
    assert "alert-danger" in field.get_attribute("class").split(), f"Поле '{field_id}' должно быть подсвечено красным."

def test_purchase(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Ожидание загрузки страницы
    wait_for_element(driver, By.CSS_SELECTOR, 'input[name="first-name"]')
    print("Страница загружена, форма доступна для заполнения.")

    # Заполнение полей формы
    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }
    fill_form_fields(driver, form_data)

    # Нажатие на кнопку отправки формы
    submit_button = wait_for_element(driver, By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Проверка успешной валидации полей
    for field_name in form_data.keys():
        validate_field_success(driver, field_name)

    # Проверка ошибки в поле zip-code
    validate_field_error(driver, "zip-code")
