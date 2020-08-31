from selenium import webdriver
#  from selenium.webdriver.common.by import By
"""automatically manages drivers for different browsers"""
from webdriver_manager.chrome import ChromeDriverManager
import time

"""Creating a web-driver object and assigning it to driver """
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://pythonprogramming.net/")
time.sleep(2)
"""Get all the cookies and store it in a cookies dict"""
cookies_dict = driver.get_cookies()
print(cookies_dict)
driver.add_cookie({'domain': '.pythonprogramming.net', 'expiry': 1598836109, 'httpOnly': False, 'name': '_dummy', 'path': '/', 'secure': False, 'value': '1892'})
print(cookies_dict)

driver.quit()
