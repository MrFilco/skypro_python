# lesson7/page_objects/inventory_page.py

from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver  # Инициализация WebDriver в классе

    def add_items_to_cart(self, item_ids):
        for item_id in item_ids:
            self.driver.find_element(By.ID, item_id).click()

    def go_to_cart(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
