# -*- coding: utf-8 -*-
"""
Created on Wed May 12 01:40:49 2021

@author: slamb
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("chromedriver.exe")  

#driver.get("https://www.mohfw.gov.in/")

driver.get("https://www.techwithtim.net/")

search = driver.find_element_by_name("s")
search.clear()
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    print(main.text)
    
finally:
    driver.quit()

#print(driver.title)

#driver.quit()