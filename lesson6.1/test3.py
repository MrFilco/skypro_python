import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    """Инициализация браузера Chrome перед тестами."""
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()

def login(driver, username, password):
    """Авторизация на сайте."""
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

def add_items_to_cart(driver, items):
    """Добавление товаров в корзину."""
    for item in items:
        driver.find_element(By.ID, item).click()

def fill_checkout_information(driver, first_name, last_name, postal_code):
    """Заполнение формы для оформления заказа."""
    driver.find_element(By.ID, "first-name").send_keys(first_name)
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)
    driver.find_element(By.ID, "continue").click()

def get_total_amount(driver):
    """Получение общей суммы заказа."""
    total_text = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    ).text
    return total_text.split()[-1]

def test_purchase(driver):
    # Открытие сайта
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    login(driver, "standard_user", "secret_sauce")

    # Добавление товаров в корзину
    items_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    add_items_to_cart(driver, items_to_add)

    # Переход в корзину и оформление заказа
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # Заполнение данных для заказа
    fill_checkout_information(driver, "Имя", "Фамилия", "12345")

    # Проверка общей суммы заказа
    total_amount = get_total_amount(driver)
    assert total_amount == "$58.29", f"Expected total to be $58.29 but was {total_amount}"
