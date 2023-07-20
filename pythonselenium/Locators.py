from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("/Users/ashishshukla/Downloads/chromedriver")
driver =webdriver.Chrome(service= service_obj, options=options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

#ID, Xpath, CSSSelector, ClassName, name, link text

driver.find_element(By.NAME, "email").send_keys("Hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test@123")
driver.find_element(By.ID, "exampleCheck1").click()

#xpath=   #//tagname=[@attribute='value']  input[@type=submit]

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ashish")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME,'alert-success').text
print(message)

assert 'success' in message



#cssselector   remove // and @ from xpath, that is cssselector
#tagname=[attribute='value']


