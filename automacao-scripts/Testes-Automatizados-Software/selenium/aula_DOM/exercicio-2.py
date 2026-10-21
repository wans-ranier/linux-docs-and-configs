import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time


# Carrega as variáveis do .env
load_dotenv()
driver_path = os.environ.get('PATH_DRIVE_BROWSER')
service = Service(driver_path)
driver = webdriver.Firefox(service=service)

try:
    driver.get()


finally:
    driver.quit()