from selenium import webdriver
from selenium.webdriver.common.by import By

"""automatically manages drivers for different browsers"""
from webdriver_manager.chrome import ChromeDriverManager
import time

"""Creating a web-driver object and assigning it to driver """
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(7)
driver.maximize_window()

"""To handle auth popup pass in the username and password along with the url"""
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(2)

driver.quit()