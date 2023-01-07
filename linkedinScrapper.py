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


i = 0
search = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
search.send_keys("Python")
search.send_keys(Keys.RETURN)
time.sleep(4)
Click1 = driver.find_element(By.CLASS_NAME,"reusable-search__result-container")
Click1.click()
time.sleep(4)

def url():
    url = driver.current_url
    return url
jobs_id = []
def alljobidonpage():
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    target = soup.find("ul",class_="scaffold-layout__list-container")
    target2 = target.find_all("li",{"data-occludable-job-id":True})
    for a in target2:
        rep = a.get("data-occludable-job-id")
        jobs_id.append(rep)
    return jobs_id
    
def max_lengthofjob():
    soup = BeautifulSoup(driver.page_source, "html.parser")
    max_length = soup.find_all("li",{"data-test-pagination-page-btn":True})
    max_length_cleared=[]
    for b in max_length:
        max_length_cleared.append(b['data-test-pagination-page-btn'])
    return max_length_cleared[-1]
b = int(max_lengthofjob())
url1 = url()
while(i<b*25):
    url2 = "https://www.linkedin.com/jobs/search/?currentJobId=3405487508&geoId=102105699&keywords=Python%20Developer&start={0}".format(str(i))
    driver.get(url2)
    time.sleep(1)
    alljobidonpage()
    i += 25
#get job id 
#job id sini aldığında aynı zamanda scrap işlemini başlat
#alljobindonepage fonksiyonunun içine scrap profile işlemini koyarım
#2.ekranda ise bu işlemi başlatırım
#bu kısımda ise her seferinde job_id nin uzunluğunu alırım
#ve sonra alljobindonepage tekrar çalıştıktan sonra 2.kez uzunluğunu alırım
#ve for döngüsünün başlangıcını ilk değer sonunu ise 2.kez uzunluğuna atarım
# 0, 25,25 50,50 75 ,75 100 ,100 125, 125 150, bu çok saçma oldu 
def scrap_profile(id):
    driver.get("https://www.linkedin.com/jobs/view/{0}".format(str(id)))
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
    print(pagesource2)

    print(job)

    for jobdesc in job:
        print(jobdesc.text)
   # for li in pagesource2:
    #    print(li.text,end="")
for jobs in jobs_id:
    print(len(jobs_id))
    try:
     print(scrap_profile(jobs))
    except:
        print("somethingHappened")
        print(jobs)