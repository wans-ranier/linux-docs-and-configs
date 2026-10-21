import os
from dotenv import load_dotenv
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

load_dotenv()
driver_path = os.environ.get('PATH_DRIVE_BROWSER')
service = Service(driver_path)
driver = webdriver.Firefox(service=service)

driver.get("https://www.google.com")

#time.sleep()
print(selenium.__version__)
driver.quit()