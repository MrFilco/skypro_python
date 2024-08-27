import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage  
from page_objects.inventory_page import InventoryPage
from page_objects.checkout_page import CheckoutPage

@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()

def test_purchase(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page = CheckoutPage(driver)

    # Открытие сайта и авторизация
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Добавление товаров в корзину
    items_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    inventory_page.add_items_to_cart(items_to_add)
    inventory_page.go_to_cart()

    # Переход к оформлению заказа
    driver.find_element(By.ID, "checkout").click()
    checkout_page.fill_checkout_information("Имя", "Фамилия", "12345")

    # Проверка общей суммы заказа
    total_amount = checkout_page.get_total_amount()
    assert total_amount == "Total: $58.29", f"Expected total to be 'Total: $58.29' but was {total_amount}"