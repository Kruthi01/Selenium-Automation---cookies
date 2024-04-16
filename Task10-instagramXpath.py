#importing webdriver from selenium
from selenium import webdriver
#importing By module from selenium webdriver
from selenium.webdriver.common.by import By
#importing time module
import time
#initializing variable for chrome browser calling
driver=webdriver.Chrome()
#giving sleep for us to view the page and understand the actions
time.sleep(5)
#getting webpage
a=driver.get("https://www.instagram.com/guviofficial/")
time.sleep(5)
#storing count of followers & following using Xpath and printing them
followers= driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span')
print("Total follower:" +followers.text)
following=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button')
print("Total followings:" +following.text)
#closing it
driver.quit()
