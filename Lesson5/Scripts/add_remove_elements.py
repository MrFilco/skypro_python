from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

def add_remove_elements(browser):
    driver = None
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    
    for _ in range(5):
        add_button.click()
    
    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
    print(f"Number of Delete buttons: {len(delete_buttons)}")
    
    driver.quit()

# Run for both browsers
add_remove_elements('chrome')
add_remove_elements('firefox')
