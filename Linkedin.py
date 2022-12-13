from ast import Return
from cgitb import text
import click
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from openpyxl import Workbook, load_workbook

PATH = "D:\ChromeDriver\chromedriver.exe"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=r'D:\ChromeDriver\chromedriver.exe')
driver.get("https://www.linkedin.com")
time.sleep(5)
#session_key
#session_password
#a = driver.find_element(by=By.CLASS_NAME,target="search-global-typeahead__input always-show-placeholder")
b = driver.find_element(By.ID, "session_key")
c = driver.find_element(By.ID, "session_password")
d = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
b.send_keys("email")
c.send_keys("password")
d.click()
time.sleep(5)
#baban = input("Lütfen aratmak isytediğiniz şeyi giriniz")
search = driver.find_element(By.XPATH,"//input[@aria-label='Arama Yap']")
search.send_keys("Python")
search.send_keys(Keys.RETURN)
time.sleep(6)
e= driver.find_element(By.CLASS_NAME, "app-aware-link")
e.click()
