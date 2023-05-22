import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/execute_script.html'
try:
    browser = webdriver.Firefox()
    browser.get(link)
    value = int(browser.find_element(By.ID, 'input_value').text)
    answer = math.log(abs(12 * math.sin(value)))
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(answer)
    input = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    input.click()
    input = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.click()
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
