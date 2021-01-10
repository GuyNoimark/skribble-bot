from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC


import pickle
import time
import datetime
import logging

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)

def login(name):

    driver.get('https://skribbl.io/')


    #Enter name, choose hebrew and logs
    driver.find_element_by_xpath('//*[@id="inputName"]').send_keys(name)
    driver.find_element_by_xpath('//*[@id="loginLanguage"]/option[11]').click()
    driver.find_element_by_xpath('//*[@id="formLogin"]/button[1]').click()





    





def getWord(time):
    timeToWait = int(time) + 5
    WebDriverWait(driver, timeToWait).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='overlay']/div/div[1]")))

    result = driver.find_element(By.XPATH, "//*[@id='overlay']/div/div[1]")
    return result.text.split(": ",1)[1]




while True:

    login('G')
    
    WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="containerLogoSmall"]/div[1]/a/img')))

    numberOfPlayers = len(driver.find_elements_by_class_name('player'))
    print(numberOfPlayers)
    if(numberOfPlayers < 3):
        continue
    
    print("Playing")
    timer = driver.find_element_by_id('timer').text
    print(timer)
    word = getWord(timer)
    print(word)
        # if getWord is None:
        #     continue

        # print(getWord)
