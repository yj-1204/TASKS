
from openpyxl import Workbook
from bs4 import BeautifulSoup

from selenium import webdriver
a=[['NAME',"CATEOGARY",'RATING']]

for i in range(1,5):
    driver= webdriver.Chrome()
    u=('https://www.myntra.com/shoes?p='+str(i))
    driver.get(u)
    s=BeautifulSoup(driver.page_source,'html.parser')
    r=s.find_all('div',{'class':'product-productMetaInfo'})
    r1=s.find_all('div',{'class':'product-ratingsContainer'})



    for j in range(len(r1)):
        e=r[j].h3.text
        f=r[j].h4.text
        g=r1[j].span.text
        l=f.split()
        if 'Sneakers' in f.split():
            a.append([e,f,g])
        else:
            pass
    
wb = Workbook() 
ws = wb.active
for row in a:
    ws.append(row)
wb.save('RESULT.xlsx') 
