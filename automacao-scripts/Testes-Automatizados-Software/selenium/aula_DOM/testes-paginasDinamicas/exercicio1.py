import os                                    
from dotenv import load_dotenv              
from selenium import webdriver
from selenium.webdriver.firefox.service import Service  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
driver_path = os.environ.get('PATH_DRIVE_BROWSER')
service = Service(driver_path)

driver = webdriver.Firefox(service=service)

try:
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.ID, "reveal"))).click()
    campo = wait.until(EC.visibility_of_element_located((By.ID, "revealed")))
    campo.send_keys("Conteúdo carregado!")
except TimeoutException:
    driver.save_screenshot("timeout.png")
    raise
finally:
    driver.quit()
