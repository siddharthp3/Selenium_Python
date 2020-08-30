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
driver.get("http://demo.guru99.com/test/delete_customer.php")

driver.find_element(By.NAME, "submit").click()
alert = driver.switch_to.alert # Switches to the JS alert
print(alert.text) # Prints the text of the alert
#alert.accept() # Accepts the alert
alert.dismiss() # Dismisses the alert

driver.switch_to.default_content() # Returns the control back to web page


time.sleep(3)
driver.quit()

