import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

# Carrega as variáveis do .env
load_dotenv()

# Recupera o caminho do geckodriver a partir da variável de ambiente
driver_path = os.environ.get('PATH_DRIVE_BROWSER')

# Cria o Service com o caminho
service = Service(driver_path)

# Inicializa o driver do Firefox
driver = webdriver.Firefox(service=service)

# Acessa uma página de teste
driver.get("https://www.example.com/")

# Agora podemos usar o driver normalmente
campo_id = driver.find_element(By.ID, "my-text-id")
campo_name = driver.find_element(By.NAME, "my-text")
campo_css = driver.find_element(By.CSS_SELECTOR, "input#my-text-id")

print(campo_id.get_attribute("placeholder"))

# Fechar o navegador
driver.quit()