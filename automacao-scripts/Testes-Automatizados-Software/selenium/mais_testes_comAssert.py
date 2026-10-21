import selenium
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time


# Carrega as variáveis do .env
load_dotenv()

# Recupera o caminho do driver a partir da variável de ambiente
driver_path = os.environ.get('PATH_DRIVE_BROWSER')

# Cria o Service com o caminho
service = Service(driver_path)

driver = webdriver.Firefox(service=service)

driver.get("https://www.selenium.dev/")
# Automação: executa uma ação
print(driver.title)
# Teste: verifica uma expectativa
assert "Selenium" in driver.title
assert driver.current_url.startswith("https://")