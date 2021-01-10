from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

import pickle
import time
import datetime

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://skribbl.io/')
driver.implicitly_wait(10)


