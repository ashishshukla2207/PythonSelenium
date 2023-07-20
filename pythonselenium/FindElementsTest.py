import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("/Users/ashishshukla/Downloads/chromedriver")
driver =webdriver.Chrome(service= service_obj, options=options)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)

countries=(driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a"))
print(len(countries))

for country in countries:
    if country.text== "India":
        print(country)
        country.click()
        break

#compare the entered vaue

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"