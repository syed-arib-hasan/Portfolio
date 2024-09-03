from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

chrome_driver_path = r"D:\evidence\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4015935340&geoId=106215326&keywords=data%20analyst&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true")

job_count=int(driver.find_element(By.CLASS_NAME,"results-context-header__job-count").text)
for i in range(27):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i+=1
    try:
        x=driver.find_element(By.XPATH,'//*[@id="main-content"]/section[2]/button')
        x.click()
        time.sleep(3)
    except:
        pass
        time.sleep(4)

company_name=[]
title_name=[]
links=[]
for j in range (job_count):
    try:
        company=driver.find_elements(By.CLASS_NAME,"base-search-card__subtitle")[j].text
        company_name.append(company)
        title=driver.find_elements(By.CLASS_NAME,"base-search-card__title")[j].text
        title_name.append(title)
        link=driver.find_elements(By.CLASS_NAME,"base-card__full-link")[j]
        links.append(link.get_attribute("href"))
    except IndexError:
        print("Done")

company_final=pd.DataFrame(company_name,columns=["Company"])
title_final=pd.DataFrame(title_name,columns=["title"])
output=company_final.join(title_final)
output.to_csv("LinkedIn JOb List")

time.sleep(100)
