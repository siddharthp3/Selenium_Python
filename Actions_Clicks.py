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
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

element = driver.find_element(By.CSS_SELECTOR, "span.context-menu-one")

"""Creating an object of ActionsChains Class. ActionChains takes driver as a parameter and Select takes web element 
as a parameter"""
action_chains = ActionChains(driver)

action_chains.context_click(element).perform()  #performs right click on the element passed
context_menu_items = driver.find_elements(By.CSS_SELECTOR,"li.context-menu-icon")
for item in context_menu_items:
    print(item.text)
    if item.text == "Copy":
        item.click()
        break

time.sleep(3)

driver.quit()
