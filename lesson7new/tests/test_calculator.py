import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.calculator_page import CalculatorPage

@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()

def test_calculator_operation(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.load()

    calculator_page.set_delay(45)
    calculator_page.press_buttons(["7", "+", "8", "="])
    calculator_page.wait_for_result("15")

    screen_text = calculator_page.get_screen_text()
    assert screen_text == "15", f"Ожидался результат 15, но получено '{screen_text}'"