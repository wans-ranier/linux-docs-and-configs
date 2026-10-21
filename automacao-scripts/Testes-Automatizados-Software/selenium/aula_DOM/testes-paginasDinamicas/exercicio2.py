import os                                    
from dotenv import load_dotenv              
from selenium import webdriver
from selenium.webdriver.firefox.service import Service  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

load_dotenv()
driver_path = os.environ.get('PATH_DRIVE_BROWSER')
service = Service(driver_path)

driver = webdriver.Firefox(service=service)

try:
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html")

    original = driver.current_window_handle
    print(f"aba original: {original.title} e {driver.title}")

    driver.switch_to.new_window("tab")
    driver.get("https://www.selenium.dev/")
    nova_aba = driver.current_window_handle
    print(f"aba nova: {nova_aba.title} e {driver.title}")

    assert "Selenium" in driver.title
    driver.close()

    driver.switch_to.window(original)
    
    
except TimeoutException:
    driver.save_screenshot("timeout.png")
    raise
finally:
    driver.quit()
