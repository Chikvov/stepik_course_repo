import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

cur_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(cur_dir, 'empty.txt')
link = 'http://suninjuly.github.io/file_input.html'
try:
    browser = webdriver.Firefox()
    browser.get(link)
    browser.find_element(By.NAME, 'firstname').send_keys('First Name')
    browser.find_element(By.NAME, 'lastname').send_keys('Last Name')
    browser.find_element(By.NAME, 'email').send_keys('my@email.com')
    browser.find_element(By.NAME, 'file').send_keys(file_path)
    browser.find_element(By.CLASS_NAME, "btn").click()
finally:
    time.sleep(10)
    browser.quit()
