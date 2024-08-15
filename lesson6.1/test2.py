import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    """Инициализация браузера Chrome перед началом тестов."""
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()

def wait_for_clickable(driver, by, value, timeout=10):
    """Ожидание, пока элемент станет кликабельным."""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, value))
    )

def wait_for_text_in_element(driver, by, value, text, timeout=70):
    """Ожидание, пока в элементе появится нужный текст."""
    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element((by, value), text)
    )

def set_delay(driver, delay_value):
    """Устанавливает значение задержки в калькуляторе."""
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(str(delay_value))
    assert delay_input.get_attribute('value') == str(delay_value), f"Значение задержки не установлено корректно. Ожидалось: {delay_value}"

def press_calculator_buttons(driver, buttons):
    """Нажимает указанные кнопки на калькуляторе."""
    for button in buttons:
        button_element = wait_for_clickable(driver, By.XPATH, f"//span[text()='{button}']")
        button_element.click()

def get_calculator_screen_text(driver):
    """Получает текст, отображаемый на экране калькулятора."""
    return driver.find_element(By.CSS_SELECTOR, "div.screen").text.strip()

def test_purchase(driver):
    # Открытие страницы калькулятора
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Установка задержки в 45 мс
    set_delay(driver, 45)

    # Нажатие кнопок 7, +, 8, =
    press_calculator_buttons(driver, ["7", "+", "8", "="])

    # Ожидание результата "15" на экране
    wait_for_text_in_element(driver, By.CSS_SELECTOR, "div.screen", "15")

    # Получение текста с экрана и проверка результата
    screen_text = get_calculator_screen_text(driver)
    print(f"Screen text is: {screen_text}")
    assert screen_text == "15", f"Ожидался результат 15, но получено '{screen_text}'"
