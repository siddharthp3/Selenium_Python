from selenium import webdriver

"""automatically manages drivers for different browsers"""
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://www.reddit.com")
# driver.get_screenshot_as_file("C:\\Users\\siddharthp3\\PycharmProjects\\Selenium_Tests\\Selenium_Python\\duckduckgo.png")
# driver.save_screenshot("C:\\Users\\siddharthp3\\PycharmProjects\\Selenium_Tests\\Selenium_Python\\duckduckgo.png")

"""Full screenshot, requires headless mode"""
screen = lambda x: driver.execute_script("return document.body.parentNode.scroll" + x)
driver.set_window_size(screen("Width"), screen("Height"))
driver.find_element_by_tag_name('body').screenshot("reddit.png")
driver.quit()
