import time


from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/cats.html'
try:
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.get(link)
    element = browser.find_element(By.ID, "button")
finally:
    time.sleep(2)
    browser.quit()
