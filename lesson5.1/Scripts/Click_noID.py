from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_dynamic_button(browser):
    driver = None
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    
    driver.get("http://uitestingplayground.com/dynamicid")
    wait = WebDriverWait(driver, 10)
    dynamic_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary')]")))
    dynamic_button.click()
    
    driver.quit()

# Run for both browsers
for _ in range(3):
    click_dynamic_button('chrome')
    click_dynamic_button('firefox')
