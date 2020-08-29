from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
"""automatically manages drivers for different browsers"""
from webdriver_manager.chrome import ChromeDriverManager
import time

"""Creating a web-driver object and assigning it to driver """
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(8)
"""gets the entered URL"""
driver.get("https://bestvpn.org/html5demos/drag/")


"""Creating an object of ActionsChains Class. ActionChains takes driver as a parameter and Select takes web element 
as a parameter"""
action_chains = ActionChains(driver)

source = driver.find_element(By.LINK_TEXT, "ExpressVPN")
target = driver.find_element(By.ID, "bin")

# action_chains.drag_and_drop(source,target).perform()  # Drag the source and drop it on the target
action_chains.click_and_hold(source).move_to_element(target).release().perform()  # Click and hold the source and move it to the target and release

time.sleep(3)

driver.quit()
