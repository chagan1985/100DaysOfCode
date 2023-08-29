###################################
#
# 100 Days of code bootcamp 2022
# (Udemy course by Angela Yu)
# 
# Day 48 exercise - Christopher Hagan
#
###################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ARTICLES_COUNT_CSS = "#articlecount > a:nth-child(1)"

driver = webdriver.Firefox()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_elements(By.CSS_SELECTOR, ARTICLES_COUNT_CSS)

print(f"Article count = {count[0].text}")

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.quit()
