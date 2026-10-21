import os                                    
from dotenv import load_dotenv              
from selenium import webdriver
from selenium.webdriver.firefox.service import Service  
from selenium.webdriver.common.by import By

load_dotenv()
driver_path = os.environ.get('PATH_DRIVE_BROWSER')
service = Service(driver_path)

driver = webdriver.Firefox(service=service)


def coletar_links(driver):
    """Coleta todos os links da página atual."""
    registros = []
    # find_elements retorna uma lista de todos os <a> da página
    for link in driver.find_elements(By.TAG_NAME, "a"):
        nome = link.text.strip()              # texto visível do link
        url = link.get_attribute("href")      # URL do link
        # Descartar itens incompletos (sem texto ou sem href)
        if nome and url:
            registros.append({"nome": nome, "url": url})
    return registros


try:
    # Navegar para a página
    driver.get("https://www.selenium.dev/")

    # Espera implícita para elementos carregarem
    driver.implicitly_wait(5)

    # Coletar dados
    dados = coletar_links(driver)

    # --- TESTES COM ASSERT ---
    # Teste 1: encontrou links
    assert len(dados) > 0, "Nenhum link coletado!"

    # Teste 2: todos os itens completos
    assert all(x["nome"] and x["url"] for x in dados), \
        "Existem links com campos vazios!"

    # Teste 3: URLs absolutas
    assert all(x["url"].startswith("http") for x in dados), \
        "Existem URLs relativas!"

    # --- Resultados ---
    print("Total de links:", len(dados))
    print("\n=== 3 PRIMEIROS ===\n")
    for i, item in enumerate(dados[:3], start=1):
        print(f"{i}. {item['nome']}")
        print(f"   {item['url']}")
        print("-" * 40)

    print("\n🎉 TESTES PASSARAM!")

finally:
    # finally garante que o navegador fecha mesmo se der erro
    driver.quit()