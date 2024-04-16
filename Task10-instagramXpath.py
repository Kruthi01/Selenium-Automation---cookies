from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
time.sleep(5)
a=driver.get("https://www.instagram.com/guviofficial/")
time.sleep(5)
followers= driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span')
print("Total follower:" +followers.text)
following=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button')
print("Total followings:" +following.text)
driver.quit()