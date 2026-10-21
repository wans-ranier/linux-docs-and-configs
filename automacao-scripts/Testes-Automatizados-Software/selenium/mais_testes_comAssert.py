import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

load_dotenv()
driver_path = os.environ.get('PATH_DRIVE_BROWSER')
service = Service(driver_path)
driver = webdriver.Firefox(service=service)

driver.get("https://www.selenium.dev/")
# Automação: executa uma ação
print(driver.title)
# Teste: verifica uma expectativa
assert "Selenium" in driver.title
assert driver.current_url.startswith("https://")