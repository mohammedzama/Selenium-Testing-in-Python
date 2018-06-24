#WE ARE GOING TO SIGNUP FACEBOOK USING PYTHON SCRIPT

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import calendar
os.system("cls")
Fname=input("Enter your FirstName:\t")
Sname=input("Enter your Surname:\t")
Email=input("Enter your Email or Mobile number:\t")
CEmail=input("Enter your Confirm Email or Mobile number:\t")
password=input("Enter your password to Set:\t")
DOB=input("Enter your Date of Birth:\t")
Gender=input("Enter the Sex Male/Female:\t")
day=DOB[0]+DOB[1]
month=DOB[2]+DOB[3]
year=DOB[4]+DOB[5]+DOB[6]+DOB[7]
driver=webdriver.Firefox()
driver.get("https://en-gb.facebook.com/")
assert "Facebook" in driver.title
driver.find_element_by_xpath('//*[@id="u_0_j"]').send_keys(Fname)
driver.find_element_by_xpath('//*[@id="u_0_l"]').send_keys(Sname)
driver.find_element_by_xpath('//*[@id="u_0_o"]').send_keys(Email)
driver.find_element_by_xpath('//*[@id="u_0_v"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="u_0_r"]').send_keys(CEmail)
dt=Select(driver.find_element_by_css_selector('#day'))
dt.select_by_value(day)
mt=Select(driver.find_element_by_css_selector('#month'))
mt.select_by_visible_text('Jan')
yt=Select(driver.find_element_by_css_selector('#year'))
yt.select_by_value(year)
#driver.find_element_by_css_selector('#u_0_z > span:nth-child(1) > label').click()
driver.find_element_by_css_selector('span._5k_2:nth-child(2) > label:nth-child(2)').click()
driver.find_element_by_xpath('//*[@id="u_0_11"]').click()
parent=driver.window_handles
print(parent)