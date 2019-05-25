#!/usr/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# contact_name must be what exact name of the contact
contact_name = 'he'
no_of_times = 200
# The message to be send
message = 'hello'


if not contact_name:
    raise ValueError('Contact name is empty')

if not message:
    raise ValueError('Message is empty')

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")
time.sleep(30)
search_bar = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input")
search_bar.clear()
search_bar.send_keys(contact_name)
search_bar.send_keys(Keys.RETURN)
for i in range(0, no_of_times):
    message_bar = driver.find_element_by_xpath(
        "//*[@id='main']/footer/div[1]/div[2]/div/div[2]"
    )
    message_bar.clear()
    message_bar.send_keys(message)
    message_bar.send_keys(Keys.RETURN)
driver.close()
