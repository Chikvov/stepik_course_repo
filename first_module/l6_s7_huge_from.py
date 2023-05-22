import time


from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/huge_form.html"
try:
    browser = webdriver.Firefox()
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, "input")
    for elem in elements:
        elem.send_keys("aaa")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
