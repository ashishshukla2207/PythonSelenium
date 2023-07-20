from selenium import webdriver

from selenium.webdriver.chrome.service import Service

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("/Users/ashishshukla/Downloads/chromedriver")
driver =webdriver.Chrome(service= service_obj, options=options)
driver.maximize_window()

driver.get("https://www.geeksforgeeks.org/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.apple.com/in")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
#driver.close()

driver.close() #new change

