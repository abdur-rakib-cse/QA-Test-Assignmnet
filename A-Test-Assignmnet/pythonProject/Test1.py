import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChormeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChormeService(ChromeDriverManager().install()))

driver.get("https://www.google.com")
time.sleep(2)
driver.close()
driver.quit()
print(" Done ")