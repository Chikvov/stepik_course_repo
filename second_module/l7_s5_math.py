import time
import math


from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'https://suninjuly.github.io/math.html'
try:
    browser = webdriver.Firefox()
    browser.get(link)
    value = browser.find_element(By.ID, 'input_value').text
    answer = math.log(abs(12 * math.sin(int(value))))
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(answer)
    input = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    input.click()
    input = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    input.click()
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
