import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time
import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Recupera o caminho do driver a partir da variável de ambiente
driver_path = os.environ.get('PATH_DRIVE_BROWSER')

# Cria o Service com o caminho
service = Service(driver_path)

driver = webdriver.Firefox(service=service)

driver.get("https://www.google.com")

#time.sleep()
print(selenium.__version__)
driver.quit()