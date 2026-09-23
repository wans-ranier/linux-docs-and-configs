from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

service = Service("/home/wans/Documentos/geckodriver-v0.37.1-linux64/geckodriver")

def test_selenium_navigationOnFireFox():
    driver = webdriver.Firefox(service=service)
    try:
        # 1. Abre https://www.selenium.dev/
        driver.get("https://www.selenium.dev/")

        # 2. Imprime título e URL
        print("O Título:", driver.title)
        print("URL:", driver.current_url)
        
        assert "Selenium" in driver.title
        assert driver.current_url.startswith("https://")
        assert driver.current_url.endswith("selenium.dev/")
                
        # 3. Navega para a documentação do WebDriver
        driver.get("https://www.selenium.dev/documentation/webdriver/")
        assert driver.current_url.endswith("webdriver/")

        # 4. Usa back() e forward() e imprime o título em cada etapa
        driver.back()
        print("Título após back():", driver.title)
        assert driver.current_url.startswith("https://")
        time.sleep(5)


        driver.forward()
        print("Título após forward():", driver.title)
        assert driver.current_url.endswith("/documentation/webdriver/")
        time.sleep(5)

        
    finally:
        # 5. Finaliza com driver.quit()
        driver.quit()

if __name__ == "__main__":
    test_selenium_navigationOnFireFox()

    