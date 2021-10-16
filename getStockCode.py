from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import time

driver= webdriver.Chrome("C:/WebDriver/bin/chromedriver.exe")
driver.get("https://www.idx.co.id/perusahaan-tercatat/profil-perusahaan-tercatat/")

Select(driver.find_element(By.XPATH,"//select[@name='companyTable_length']")).select_by_value('100')
time.sleep(1.2)
f=open("C:/Users/Astrowest/Documents/Persahaman/KodeEmiten.txt",'w+')

for n in range(8):
    if(n>0):
        driver.find_element(By.XPATH,"//a[@class='paginate_button next']").send_keys(Keys.ENTER)
        time.sleep(1)
    for emitenCode in driver.find_elements(By.XPATH,"//tbody/tr[@role='row']/td[2]"):
        print(emitenCode.text)
        time.sleep(0.3)
        f.write(emitenCode.text+"\n")
f.close()