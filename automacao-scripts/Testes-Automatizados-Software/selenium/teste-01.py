import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

service = Service("/home/wans/Documentos/geckodriver-v0.37.1-linux64/geckodriver")
driver = webdriver.Firefox(service=service)

driver.get("https://www.google.com")

time.sleep(5)
print(selenium.__version__)
driver.quit()