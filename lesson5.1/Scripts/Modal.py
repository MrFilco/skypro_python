from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


import time

def handle_modal(browser):
    driver = None
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    
    driver.get("http://the-internet.herokuapp.com/entry_ad")
    time.sleep(2)  # Wait for modal to appear
    close_button = driver.find_element(By.XPATH, "//div[@class='modal-footer']/p")
    close_button.click()
    
    driver.quit()

# Run for both browsers
handle_modal('chrome')
handle_modal('firefox')
