from selenium.webdriver.common.by import By

class InventoryPage:
    def init(self, driver):
        self.driver = driver

    def add_items_to_cart(self, items):
        for item in items:
            self.driver.find_element(By.ID, item).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()