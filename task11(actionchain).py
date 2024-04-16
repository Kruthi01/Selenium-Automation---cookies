'''Drag and Drop code - for task 11'''
#importing webdriver from selenium
from selenium import webdriver
#importing actionchains from selenium webdriver
from selenium.webdriver import ActionChains
#importing By module
from selenium.webdriver.common.by import By
#initializing firefox browser
browser = webdriver.Firefox()
#Getting inside a web site
browser.get("https://jqueryui.com/droppable/")
browser.switch_to.frame(0)
#storing the element using xpath id
source_element = browser.find_element(By.XPATH, "//*[@id='draggable']")
target_element = browser.find_element(By.XPATH,"//*[@id='droppable']")
#initializing actionchains
actions = ActionChains(browser)
#performing drag and drop operation using in built functions/methods
actions.drag_and_drop(source_element,target_element).perform()
#closing it
browser.quit()
print("Successfully dragged and dropped")
