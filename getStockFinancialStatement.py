import time
from selenium import webdriver
from Stock_Research.emitenCodeList import emitenCodeList


driver= webdriver.Chrome("C:/WebDriver/bin/chromedriver.exe")
Quarter=['I','II','III','Tahunan']
Year =[2018,2019,2020,2021]
#Change the year on the link below, if you choose Tahunan then change 'TW1/TW2/TW3' being 'Audit'. and 'romans number' to 'Tahunan'
for emiten in emitenCodeList:
  wd.get('https://www.idx.co.id/Portals/0/StaticData/ListedCompanies/Corporate_Actions/New_Info_JSX/Jenis_Informasi/01_Laporan_Keuangan/02_Soft_Copy_Laporan_Keuangan//Laporan%20Keuangan%20Tahun%202019/TW3/'+emiten+'/FinancialStatement-2019-III-'+emiten+'.xlsx')
  time.sleep(5)
wd.delete_all_cookies()
wd.quit()