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
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    # Campo de texto: ID é a opção mais direta e estável
    texto = driver.find_element(By.ID, "my-text-id")
    # Senha: NAME é mais específico que apenas type=password
    senha = driver.find_element(By.NAME, "my-password")
    # Botão: CSS relativo e legível
    botao = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    print(texto.get_attribute("name"))
    print(senha.get_attribute("type"))
    print(botao.text)
    time.sleep(10)
finally:
    driver.quit()