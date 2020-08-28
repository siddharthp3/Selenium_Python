from selenium import webdriver
from selenium.webdriver.common.by import By
"""automatically manages drivers for different browsers"""
from webdriver_manager.chrome import ChromeDriverManager
import time

"""Creating a web-driver object and assigning it to driver """
driver = webdriver.Chrome(ChromeDriverManager().install())
"""Wait for all the operations implicitly"""
driver.implicitly_wait(6)

"""gets the entered URL"""
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")


"""Locators are the way to identify an HTML element on a web page"""
"""Find the locator for url, first name, last name and email and assign it to a variable"""

url = driver.find_element(By.ID, "Form_submitForm_subdomain")  # By ID
first_name = driver.find_element_by_id("Form_submitForm_FirstName")   # Inplace of By can directly use by_id method
last_name = driver.find_element(By.NAME, "LastName")  # By Name
"""
Types of locators
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
"""

"""Basic Xpath formula : Xpath=//tagname[@attribute='value'] """
email = driver.find_element(By.XPATH, "//input[@type='email']")  # By Xpath

job_title = driver.find_element(By.CSS_SELECTOR, "#Form_submitForm_JobTitle")  # By CSS Selector

"""Send keys allows us to enter required text in the text field"""
url.send_keys("DummeyUser.com")
first_name.send_keys("Dummy")
last_name.send_keys("User")
email.send_keys("DummyUser@email.com")
job_title.send_keys("SDET")
time.sleep(4)


features_link = driver.find_element(By.LINK_TEXT, "Features")  # By link text
features_link.click()

# driver.close()
"""Closes all browser windows and safely ends the session"""
driver.quit()
