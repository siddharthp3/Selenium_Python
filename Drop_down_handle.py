from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
"""automatically manages drivers for different browsers"""
from webdriver_manager.chrome import ChromeDriverManager
import time

"""Creating a web-driver object and assigning it to driver """
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()  # Maximize the screen
driver.implicitly_wait(5)

"""gets the entered URL"""
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")


"""Function to select a particular value from a drop down without using Select Class"""
def select_value(options, value):
    for item in options:
        if item.text == value:
            item.click()
            break

# """Function to select a particular value from a drop down using Select Class"""
# def select_value(web_element, visible_text):
#     select_value = Select(web_element)
#     select_value.select_by_visible_text(visible_text)
#
# """Find the industry drop down"""
# industry = driver.find_element(By.ID, "Form_submitForm_Industry")
#
# """Use the Select class and pass it the industry web element """
# industry_select = Select(industry)
# # industry_select.select_by_visible_text("Healthcare")  # By text visible on UI
# # industry_select.select_by_index(4) # By index
# industry_select.select_by_value("health")  # By HTML Attribute value
#
# country = driver.find_element(By.NAME, "Country")
# select_value(country, "Argentina")  #Selecting a drop-down value using a custom function
#
# industry_op_list = industry_select.options  # Returns a list of the options in the drop down
# for option in industry_op_list:  # for loop to print all the industry options
#     print(option.text)
# print(industry_select.is_multiple) # returns None to indicate if the drop down is not multi select

"""Selecting a drop down value without using a Select class"""
country_list = driver.find_elements(By.XPATH, "//select[@id='Form_submitForm_Country']/option")  # Returns a list of all the countries
select_value(country_list, "Bahamas")
# for country in country_list:
#     if country.text == "Bahamas":
#         country.click()
#         break

time.sleep(4)

driver.quit()
