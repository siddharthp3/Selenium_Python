from selenium import webdriver
from selenium.webdriver.common.by import By

"""automatically manages drivers for different browsers"""
from webdriver_manager.chrome import ChromeDriverManager
import time

"""Creating a web-driver object and assigning it to driver """
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(7)
driver.maximize_window()

"""gets the entered URL"""
driver.get("http://www.londonfreelance.org/courses/frames/index.html")

# driver.switch_to.frame("main")  # Switch to a particular frame
frame_element = driver.find_element(By.NAME, "main")  # Find the frame element yisng By and assign it to a frame element
driver.switch_to.frame(frame_element)  # Switch to a particular frame
frame_text = driver.find_element(By.CSS_SELECTOR, "body > h2").text
print(frame_text)

driver.switch_to.default_content() # Returns the control back to web page

driver.quit()
