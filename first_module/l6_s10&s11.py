import time


from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/registration2.html"
    # browser = webdriver.Firefox()
    browser = webdriver.Chrome()
    browser.get(link)
    input = browser.find_element(By.CSS_SELECTOR, "input[placeholder*='first name']")
    input.send_keys('First Name')
    input = browser.find_element(By.CSS_SELECTOR, "input[placeholder*='last name']")
    input.send_keys('Last Name')
    input = browser.find_element(By.CSS_SELECTOR, "input[placeholder*='email']")
    input.send_keys('my@email.com')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(2)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
