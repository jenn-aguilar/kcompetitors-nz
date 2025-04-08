from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://lalabeauty.co.nz/collections/all?sort_by=best-selling")

# Scroll to load more products (infinite scroll)
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Grab product elements
products = driver.find_elements(By.CLASS_NAME, "productgrid--item")

for product in products:
    try:
        title = product.find_element(By.CLASS_NAME, "productitem--title").text
        price = product.find_element(By.CLASS_NAME, "price--main").text
        print(f"{title} - {price}")
    except:
        continue

driver.quit()