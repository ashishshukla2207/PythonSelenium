import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("/Users/ashishshukla/Downloads/chromedriver")
driver =webdriver.Chrome(service= service_obj, options=options)
driver.implicitly_wait(5) # 5 sec is max time out, if the element is visible in 5 sec, it will proceed (3 sec saved)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

results=driver.find_elements(By.XPATH, "//div[@class='products']/div")
count= len(results)

assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()
    driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
    driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

    driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
    driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
    #time.sleep(5)