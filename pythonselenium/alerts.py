from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("/Users/ashishshukla/Downloads/chromedriver")
driver =webdriver.Chrome(service= service_obj, options=options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name="ashish"
driver.find_element(By.ID, "name").send_keys(name)

driver.find_element(By.ID, "alertbtn").click()

alert= driver.switch_to.alert

alertText = alert.text
print(alertText)
alert.accept()
#alert.dismiss()  to dismiss