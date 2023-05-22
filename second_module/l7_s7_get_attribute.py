import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/get_attribute.html'
try:
    browser = webdriver.Firefox()
    browser.get(link)
    value = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    answer = math.log(abs(12 * math.sin(int(value))))
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(answer)
    input = browser.find_element(By.ID, "robotCheckbox")
    input.click()
    input = browser.find_element(By.ID, "robotsRule")
    input.click()
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
