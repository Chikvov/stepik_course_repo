import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/redirect_accept.html'
try:
    browser = webdriver.Firefox()
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(1)
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])
    value = int(browser.find_element(By.ID, 'input_value').text)
    answer = math.log(abs(12 * math.sin(value)))
    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    time.sleep(5)
    browser.quit()
