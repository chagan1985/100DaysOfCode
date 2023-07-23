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

UPCOMING_EVENTS = ".event-widget"
UPCOMING_EVENTS_TIME_SELECTOR = f"{UPCOMING_EVENTS} time"
UPCOMING_EVENTS_NAME_SELECTOR = f"{UPCOMING_EVENTS} li a"

driver = webdriver.Firefox()

driver.get("https://www.python.org/")

upcoming_events_date = driver.find_elements(By.CSS_SELECTOR, UPCOMING_EVENTS_TIME_SELECTOR)
upcoming_events_event = driver.find_elements(By.CSS_SELECTOR, UPCOMING_EVENTS_NAME_SELECTOR)

events = {}
for i in range(len(upcoming_events_date)):
    events[i] = {
        upcoming_events_date[i].text: upcoming_events_event[i].text
    }

print(events)

driver.quit()
