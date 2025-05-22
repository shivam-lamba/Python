# -*- coding: utf-8 -*-
"""
Created on Wed May 12 02:44:08 2021

@author: slamb
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("chromedriver.exe") 

driver.get("https://www.techwithtim.net/")

link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    beg_tut = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    beg_tut.click()
    
    get_st = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    driver.back()
    driver.back()
    driver.back()
    
    
except:
    driver.quit()