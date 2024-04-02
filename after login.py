
# Switching windows between google and saucedemo

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# initialize chrome webdriver
driver = webdriver.Chrome()

#opening saucedemo
driver.get("https://www.saucedemo.com/")
#getting cookies before login
res=driver.get_cookies()
print("Before login cookie is:")
#And printing them
print(res)
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")
username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()
time.sleep(3)
#Getting cookies after login
res1=driver.get_cookies()
print("After login cookie is:")
#And printing them
print(res1)


