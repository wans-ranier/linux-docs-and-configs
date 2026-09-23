import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time


service = Service("/home/wans/Documentos/geckodriver-v0.37.1-linux64/geckodriver")
driver = webdriver.Firefox(service=service)

driver.get("https://www.selenium.dev/")
# Automação: executa uma ação
print(driver.title)
# Teste: verifica uma expectativa
assert "Selenium" in driver.title
assert driver.current_url.startswith("https://")