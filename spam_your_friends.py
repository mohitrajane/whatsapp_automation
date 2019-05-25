#!/usr/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

contact_name = "d*** anto"
no_of_times  = 200
message = "Dick Boy"

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")
time.sleep(30)
elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input")
elem.clear()
elem.send_keys(contact_name)
elem.send_keys(Keys.RETURN)
for i in range (0,no_of_times):
	msg = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
	msg.clear()
	msg.send_keys(message)
	msg.send_keys(Keys.RETURN)
driver.close()
