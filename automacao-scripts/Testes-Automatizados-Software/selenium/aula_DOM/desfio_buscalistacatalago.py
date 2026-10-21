import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

load_dotenv()
driver_path = os.environ.get('PATH_DRIVE_BROWSER')
service = Service(driver_path)
driver = webdriver.Firefox(service=service)

# --- Navegar para a página de catálogo ---
driver.get("https://quotes.toscrape.com/")

# Espera implícita
driver.implicitly_wait(5)

cards = driver.find_elements(By.CSS_SELECTOR, "div.quote")

produtos = []

# --- Percorrer cada card e extrair os dados ---
for card in cards:
    try:
        # Dado 1: texto da citação (<span class="text">)
        texto = card.find_element(By.CSS_SELECTOR, "span.text").text

        # Dado 2: autor (<small class="author">)
        autor = card.find_element(By.CSS_SELECTOR, "small.author").text

        # Dado 3: URL do autor (o link "(about)" fica logo após o small, dentro de um <a>)
        url = card.find_element(By.CSS_SELECTOR, "span > a").get_attribute("href")

        # Se a URL vier relativa, completamos com o domínio base
        if url and not url.startswith("http"):
            url = "https://quotes.toscrape.com" + url

        # --- Descartar itens incompletos ---
        if not texto or not autor or not url:
            continue  

        produtos.append({
            "texto": texto,
            "autor": autor,
            "url": url
        })
    except Exception as e:
        continue

print(f"\nTotal de itens coletados: {len(produtos)}")

print("\n=== 3 PRIMEIROS REGISTROS ===\n")

for indice, produto in enumerate(produtos[:3], start=1):
    print(f"Citação {indice}:")
    print(f"  Texto: {produto['texto']}")
    print(f"  Autor: {produto['autor']}")
    print(f"  URL:   {produto['url']}")
    print("-" * 40)

driver.quit()

print("\nDesafio concluído com sucesso!")