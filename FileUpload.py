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
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")

"""Find the element to upload the file and send the path of the file to be uploaded
Will only work if type="file" attribute is presnet 
"""
driver.find_element(By.NAME, "upfile").send_keys("C:\\Users\\siddharthp3\\Documents\\Sample.txt")

driver.find_element(By.XPATH, "//input[@type='submit']").click()

time.sleep(2)

driver.quit()