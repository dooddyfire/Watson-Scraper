
from bs4 import BeautifulSoup 
import requests 
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import re 
import pandas as pd 
from datetime import datetime
from selenium.webdriver.chrome.options import Options



import datetime
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.chrome.service import Service
from seleniumbase import Driver


#input_url = 'https://www.watsons.co.th/th/%E0%B8%AA%E0%B8%B4%E0%B8%99%E0%B8%84%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%B1%E0%B8%95%E0%B8%AA%E0%B8%B1%E0%B8%99/%E0%B8%A1%E0%B8%B2%E0%B8%AA%E0%B9%8C%E0%B8%81/c/040200'
input_url = input("Enter your url : ")


filename = input("Enter your filename : ")


# driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

start = int(input("Enter Start Page : "))
end = int(input("Enter End Page : "))


prod_lis = []
pro_item_lis = []
bought_lis = []
buy_price_lis = []
price_discount_lis = []
prod_name_lis = []
member_price_lis = []
item_link_lis = []

driver = Driver(uc=True)


for page in range(start,end+1):

    if page == 1: 
        url = input_url 
    else:    
        url = input_url +'?currentPage={}'.format(page)

    driver.get(url)


    lis = [ k for k in driver.find_elements(By.CSS_SELECTOR,'div.productContainer')]


    for i in lis:

        try:
                prod_name = i.find_element(By.CSS_SELECTOR,'h2').text
            
        except: 
                prod_name = '-'
        print('Name : ',prod_name)


        try:
                url_item= i.find_element(By.CSS_SELECTOR,'a.ClickSearchResultEvent_Class').get_attribute('href')
            
        except: 
                purl_item = '-'
        print('Link: ',url_item)
        item_link_lis.append(url_item)


        try: 
                promotion = "\n".join( list(set([k.text.strip() for k in driver.find_elements(By.CSS_SELECTOR,'div.productHighlight')])) )

        except:
                promotion = '-'
            
        print('Promotion : ',promotion)
        pro_item_lis.append(promotion)

        try:
                price = i.find_element(By.CSS_SELECTOR,'div.productOriginalPrice ').text 
                print(price)
        except: 
                price = '-'
            
        print('Price Full : ',price)
        buy_price_lis.append(price)

        try:
                dc_price = i.find_element(By.CSS_SELECTOR,'div.formatted-value').text 
            
        except:

                dc_price = '-'
        print('Discount Price : ',dc_price)
        price_discount_lis.append(dc_price)

        try:
                member_price = i.find_element(By.CSS_SELECTOR,'div.memberPrice-content').text.strip()

        except: 
                member_price = '-'

        print('Member Price : ',member_price)
        member_price_lis.append(member_price)

        try: 
                bought = i.find_element(By.CSS_SELECTOR,'div.social-proof-box').text.strip()
            
        except:
                bought = '-'

        print('Total Sell : ',bought)
        bought_lis.append(bought)

        print()

df = pd.DataFrame()
df['Name'] = prod_name_lis 
df['Pirce'] = buy_price_lis 
df['Discount Pirce'] = price_discount_lis 
df['Member Price'] = member_price_lis 
df['ขายไปแแล้ว'] = bought_lis 
df['Promotion'] = pro_item_lis 
df['Link'] = item_link_lis
df.to_excel(filename+'.xlsx')

print('Finish')