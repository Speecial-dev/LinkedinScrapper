from ast import Return
from cgitb import text
import click
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook
import pandas as pd

PATH = "D:\ChromeDriver\chromedriver.exe"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=r'D:\\ChromeDriver\\chromedriver.exe')
links = []
driver.get("https://www.linkedin.com")
driver.maximize_window()
timeout = 5
time.sleep(2)
email = ""
password = ""
b = driver.find_element(By.ID, "session_key")
c = driver.find_element(By.ID, "session_password")
d = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
b.send_keys(email)
c.send_keys(password)
d.click()
time.sleep(2)


def scrap_profile():
    driver.get("https://www.linkedin.com/jobs/view/3388085198/")
    time.sleep(2)
    soup2 = BeautifulSoup(driver.page_source, "html.parser")
    pagesource  = soup2.find(class_="jobs-unified-top-card t-14 artdeco-card mb4")
    pagesource2 = pagesource.find_all(True,{'class':['ember-view t-black t-normal',"jobs-unified-top-card__job-insight"]})
    soup3 = soup2.find(class_="hirer-card__container")
    try:
        linkofhirer = soup3.find("a",class_="app-aware-link").get("href")
        print(linkofhirer)
    except:
        print("no hirer selected in this page")
    #linkofhirer= soup3.find(class_="app-aware-link ").get("href")
    job = soup2.find("article",class_="jobs-description__container jobs-description__container--condensed")

    for jobdesc in job:
        print(jobdesc.text)
   # for li in pagesource2:
    #    print(li.text,end="")

scrap_profile()