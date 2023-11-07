import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChormeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChormeService(ChromeDriverManager().install()))

driver.get("https://www.google.com")
googleSearchBox =driver.find_element(By.ID, "APjFqb")
googleSearchBox.send_keys("Automation")
googleSearchBox.send_keys(Keys.RETURN)
# # driver.find_element(By.NAME, "btnK").click()

# time.sleep(2)

driver.get("https://trytestingthis.netlify.app/index.html")

driver.find_element(By.ID, "fname").send_keys("Abdur")
driver.find_element(By.ID, "lname").send_keys("Rakib")
time.sleep(5)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(5)
driver.quit()