


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pathlib import Path
from bs4 import BeautifulSoup

# initialize chrome webdriver
driver = webdriver.Chrome()

#opening saucedemo
driver.get("https://www.saucedemo.com/")
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")
username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()
time.sleep(3)
res= driver.title
print("Title of the webpage is:")
print(res)
res1=driver.current_url
print(res1)
print(driver.find_element(By.XPATH,"/html/body").text)

def test_html_save():
    soup = BeautifulSoup(html_content, 'html.parser') # creates a beautiful soup object 'soup'.

    html_save_path = Path(__file__).parent / ".//html_save_test.txt"

    with open(html_save_path, 'wt') as html_file:
        for line in soup.prettify():
            html_file.write(line)

test_html_save()



