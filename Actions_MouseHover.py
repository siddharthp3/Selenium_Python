from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
"""automatically manages drivers for different browsers"""
from webdriver_manager.chrome import ChromeDriverManager
import time

"""Creating a web-driver object and assigning it to driver """
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()

"""gets the entered URL"""
driver.get("https://www.spicejet.com/")
time.sleep(3)

"""Creating an object of ActionsChains Class. ActionChains takes driver as a parameter and Select takes web element 
as a parameter"""
action_chains = ActionChains(driver)


login_element = driver.find_element(By.ID, "ctl00_HyperLinkLogin")
action_chains.move_to_element(login_element).perform()  # Passing the web element to action_chains object to perform mouse hover
club_element = driver.find_element(By.LINK_TEXT, "SpiceClub Members")
action_chains.move_to_element(club_element).perform()
member_login_element = driver.find_element(By.LINK_TEXT, "Member Login")
member_login_element.click()


time.sleep(4)

driver.quit()
