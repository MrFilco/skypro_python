from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def click_class_button(browser):
    driver = None
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    
    driver.get("http://uitestingplayground.com/classattr")
    blue_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
    blue_button.click()
    
    driver.quit()

# Run three times for each browser
for _ in range(3):
    click_class_button('chrome')
    click_class_button('firefox')
