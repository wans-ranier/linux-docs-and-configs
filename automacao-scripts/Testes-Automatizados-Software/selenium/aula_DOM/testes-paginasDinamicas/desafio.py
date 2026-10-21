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
    driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframeResult")))
    driver.find_element(By.TAG_NAME, "button").click()

    alerta = wait.until(EC.alert_is_present())
    assert "alert" in alerta.text.lower()
    alerta.accept()

    driver.switch_to.default_content()
finally:
    driver.quit()