from selenium import webdriver
from selenium.webdriver.common.by import By
"""automatically manages drivers for different browsers"""
from webdriver_manager.chrome import ChromeDriverManager
import time

"""Creating a webdriver object and assigning it to driver """
driver = webdriver.Chrome(ChromeDriverManager().install())

"""Wait 5s for all the operations implicitly"""
driver.implicitly_wait(5)

"""gets the entered URL"""
driver.get("https://www.google.com/")

"""Prints the title of the webpage on the console"""
print(driver.title)

"""Find the search box to enter the required text"""
driver.find_element(By.NAME, "q").send_keys("PrivacyIO")

time.sleep(3)  # wait for the results to load
"""Store all the options in option_list"""
option_list = driver.find_elements(By.CSS_SELECTOR, "ul.erkvQe li span")

"""Using for loop select the one required and click on the same"""
for item in option_list:
    if item.text == "privacy io reddit":
        item.click()
        break

time.sleep(3)  # wait for the page to be visible
"""Close the browser window that the driver has focus of"""
# driver.close()

"""Closes all browser windows and safely ends the session"""
driver.quit()
