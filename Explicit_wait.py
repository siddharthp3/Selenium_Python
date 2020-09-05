from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
"""automatically manages drivers for different browsers"""
from webdriver_manager.chrome import ChromeDriverManager
import time

"""Creating a web-driver object and assigning it to driver """
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://app.hubspot.com/login")

"""Creating a object of webdriverwait class, passing maximum timeout of 10 secs"""
wait = WebDriverWait(driver, 10)

wait.until(ec.title_is('HubSpot Login'))  # wait until the title of the page is displayed
print(driver.title)
email = wait.until(ec.presence_of_element_located((By.ID, "username")))
email.send_keys("demo@email.com")
password = driver.find_element(By.ID, "password")
password.send_keys("demo")

sing_up = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Sign up")))  # Wait until the element is clickable
print(sing_up.text)
sing_up.click()

first_name = wait.until(ec.visibility_of_element_located((By.ID, "uid-firstName-5")))  # Wait until the element in present in DoM and also on the page
first_name.send_keys("Jane")


time.sleep(3)


driver.quit()
