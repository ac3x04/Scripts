#!/opt/homebrew/bin/python3
#title           :seleniumBot.py
#description     :This script will use the python selenium module to drive the firefox browser. It will make a google query then connected to one of the results in the query. This is to showcase the evolution of basic command line tools as bots.
#author		     :Ace Xor
#date            :2023-10-29
#version         :0.1
#usage		     :python seleniumBot.py
#notes           :The selenium library is required to run this script

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

browserInstance = webdriver.Firefox()
browserInstance.get("https://www.google.com")
searchBar = browserInstance.find_element(By.ID, "APjFqb")
action = ActionChains(browserInstance)
action.move_to_element(searchBar).click().perform()
action.send_keys("what are my browser headers").perform()
action.send_keys(Keys.RETURN).perform()
time.sleep(2)
clickLink = browserInstance.find_element(By.XPATH, "/html/body/div[5]/div/div[12]/div/div[2]/div[2]/div/div/div[4]/div/div/div[1]/div/div/span/a/div/div/span")
browserInstance.execute_script("arguments[0].scrollIntoView();", clickLink)
browserInstance.get("https://google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjjisuzuZyCAxXUKVkFHYTVB3AQFnoECBAQAQ&url=https%3A%2F%2Fmyhttpheader.com%2F&usg=AOvVaw2ec_rqK_npAtRitbkKxJFk&opi=89978449")