from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/Purujit/Desktop/facebook_bot/chromedriver")

url = 'https://www.facebook.com/'
driver.get(url)
username = 'enter username here'
password = 'enter password here'
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()
time.sleep(10)
driver.find_element_by_name('q').click()
time.sleep(3)
driver.find_element_by_name('q').send_keys('Mark Zukerberg')
time.sleep(3)
driver.find_element_by_name('q').send_keys('\n')
