import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects2.html'
try:
    browser = webdriver.Firefox()
    browser.get(link)
    n1 = browser.find_element(By.ID, 'num1').text
    n2 = browser.find_element(By.ID, 'num2').text
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(int(n1) + int(n2)))
    browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    time.sleep(5)
    browser.quit()
