from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())

"""
implicitly_wait is a dynamic wait only for web elements.
The wait is applied for all the web elements
"""
driver.implicitly_wait(10)

driver.get("https://app.hubspot.com/login")

driver.find_element(By.ID, "username").send_keys("Admin")  # implicitly_wait will be applied for username
driver.find_element(By.ID, "password").send_keys("Admin")  # implicitly_wait will be applied for password

driver.quit()
