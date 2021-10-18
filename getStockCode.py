from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome("C:/WebDriver/bin/chromedriver.exe")
driver.get("https://www.idx.co.id/perusahaan-tercatat/profil-perusahaan-tercatat/")
Select(driver.find_element(By.XPATH,"//select[@name='companyTable_length']")).select_by_value('100')
f=open("C:/Users/Astrowest/Documents/GitHub/Stock_Research/emitenCodeList.py",'w+')
emitenCodeList=[]
WebDriverWait(driver,10).until(lambda driver: len(driver.find_elements(By.XPATH,"//tbody/tr[@role='row']/td[2]")) == 100)
for n in range(8):
    if(n>0):
        driver.find_element(By.XPATH,"//a[@class='paginate_button next']").send_keys(Keys.ENTER)
        WebDriverWait(driver,10).until(lambda driver : int(driver.find_element(By.XPATH,"//tbody/tr[@role='row'][1]/td[1]").text ) > before)
    before = int(driver.find_element(By.XPATH,"//tbody/tr[@role='row'][1]/td[1]").text)
    for emitenCode in driver.find_elements(By.XPATH,"//tbody/tr[@role='row']/td[2]"):
        emitenCodeList.append(emitenCode.text)
        time.sleep(0.05)

f.write("emitenCodeList="+str(emitenCodeList))
f.close()