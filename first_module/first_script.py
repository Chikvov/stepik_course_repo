import time


from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options

# options = Options()
driver = webdriver.Firefox()
time.sleep(5)
driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(5)
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
textarea.send_keys("get()")
time.sleep(5)
sumbit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
sumbit_button.click()
time.sleep(5)
driver.quit()
