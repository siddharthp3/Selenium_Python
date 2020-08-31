from selenium import webdriver
#  from selenium.webdriver.common.by import By
"""automatically manages drivers for different browsers"""
from webdriver_manager.chrome import ChromeDriverManager
#  import time

options = webdriver.ChromeOptions()
"""Setting option for headless to true"""
options.headless = True
#  options.add_argument("--incognito")  # For running chrome in incognito mode
"""Creating a web-driver object and assigning it to driver and passing options"""
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://pythonprogramming.net/")

print(driver.title)


driver.quit()
