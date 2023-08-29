###################################
#
# 100 Days of code bootcamp 2022
# (Udemy course by Angela Yu)
# 
# Day 48 exercise - Christopher Hagan
#
###################################

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


LANGUAGE_CSS = "#langSelect-EN"
COOKIE_CSS = "#bigCookie"
STORE_CSS = "#store div"
COOKIES_COUNT_CSS = "#cookies"
STORE_ITEMS_XPATH = "//div[@class='product unlocked enabled']"

driver = webdriver.Firefox()

driver.get("https://orteil.dashnet.org/cookieclicker/")

try:
    # Wait for the element to be clickable
    language_selector = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, LANGUAGE_CSS))
    )
    language_selector.click()
except Exception as e:
    print("An error occurred:", str(e))

try:
    cookie = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, COOKIE_CSS))
    )
    cookie.click()
    click_number = 1
except Exception as e:
    print("An error occurred:", str(e))

timeout = time.time() + 5
five_min = time.time() + 300
max_cookies_per_sec = 0

while True:
    cookie.click()
    
    if time.time() > timeout:
        # Get the cookie counter information
        cookie_counter = driver.find_element(By.CSS_SELECTOR, COOKIES_COUNT_CSS).text
        cookie_count = int(cookie_counter.split(" ")[0].replace(",",""))
        cookies_per_sec = float(cookie_counter.split(": ")[1])
        if cookies_per_sec > max_cookies_per_sec:
            max_cookies_per_sec = cookies_per_sec

        # Find all elements in the store
        store_items = driver.find_element(By.CSS_SELECTOR, STORE_CSS)
        
        # Set base values for most expensice item calculation
        most_expensive_price = 0
        most_expensive_item = None

        for item in store_items.find_elements(By.XPATH, STORE_ITEMS_XPATH):
            price = int(item.find_element(By.CLASS_NAME, "price").text)

            # set the most expensive item
            if price > most_expensive_price:
                most_expensive_item = item

        # If we found an item
        if most_expensive_item is not None:
            most_expensive_item.click()


    if time.time() > five_min:
        break

print(f"The final cookie count was {cookie_count}")
print(f"The maximum cookies per sec was {max_cookies_per_sec}")

driver.quit()
