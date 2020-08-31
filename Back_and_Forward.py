from selenium import webdriver
from selenium.webdriver.common.by import By
"""automatically manages drivers for different browsers"""
from webdriver_manager.chrome import ChromeDriverManager
import time

"""Creating a web-driver object and assigning it to driver """
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://pythonprogramming.net/")
time.sleep(2)
driver.find_element(By.XPATH, "//strong[text()='Python Fundamentals']").click()

driver.back()  # Go back to the previous web page
time.sleep(2)
driver.forward()  # Go the next webpage
driver.back()
driver.refresh()  # Refresh the page
time.sleep(2)

driver.quit()
