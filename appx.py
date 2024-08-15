
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
pro2_lis = []
driver = Driver(uc=True)


for page in range(start,end+1):

    if page == 1: 
        url = input_url 
    else:    
        url = input_url +'?currentPage={}'.format(page)

    driver.get(url)


    lis = [ k for k in driver.find_elements(By.CSS_SELECTOR,'div.productContainer')]


    c = 1
    for i in lis:
        driver.get(i)

        time.sleep(5)
        try:
               btn_cookie = driver.find_element(By.CSS_SELECTOR,'btn#onetrust-accept-btn-handler')
               btn_cookie.click()
        except:
               pass

        soup = BeautifulSoup(driver.page_source,'html.parser')


        try:
                #prod_name = i.find_element(By.CSS_SELECTOR,'div.product-name').text
                prod_name = i.split("/")[-3]
        except: 
                prod_name = '-'
        print('Name : ',prod_name)
        prod_name_lis.append(prod_name)

        
        url_item= i
            

        print('Link: ',url_item)
        item_link_lis.append(url_item)


        try: 
                #promotion = "\n".join( list(set([k.text.strip() for k in driver.find_elements(By.CSS_SELECTOR,'div.coupon')])) )
                promotion = "\n".join( list(set([k.text.strip() for k in soup.find_all('e2-ecoupon-item')])) )

        except:
                promotion = '-'
            
        print('Promotion : ',promotion)
        pro_item_lis.append(promotion)

        try:
                #price = i.find_element(By.CSS_SELECTOR,'span.retail-price').text
                price = soup.find('span',{'class':'retail-price'}).text
                print(price)
        except: 
                price = '-'
            
        print('Price Full : ',price)
        buy_price_lis.append(price)

        try:
                #dc_price = i.find_element(By.CSS_SELECTOR,'span.price').text 
                dc_price = soup.find('span',{'class':'price'}).text

        except:

                dc_price = '-'
        print('Discount Price : ',dc_price)
        price_discount_lis.append(dc_price)

        try:
                member_price = soup.find_all('span',{'class':'price'})[1].text

        except: 
                member_price = '-'

        print('Member Price : ',member_price)
        member_price_lis.append(member_price)

        try: 
                #bought = i.find_element(By.CSS_SELECTOR,'div.social-proof').text.strip()
                bought = soup.find('div',{'class':'social-proof'}).text.strip()

        except:
                bought = '-'

        print('Total Sell : ',bought)
        bought_lis.append(bought)

        try: 
               pro2 = "\n".join([x.text for x in soup.find_all('div',{'class':'promotion-group'})])
               
        except:
               pro2 = '-' 
        print('promotion 2 : ',pro2)
        pro2_lis.append(pro2)
        print()
        c = c + 1

df = pd.DataFrame()
df['Name'] = prod_name_lis 
df['Pirce'] = buy_price_lis 
df['Discount Pirce'] = price_discount_lis 
df['Member Price'] = member_price_lis 
df['ขายไปแแล้ว'] = bought_lis 
df['Promotion'] = pro_item_lis 
df['Promotion 2'] = pro2_lis
df['Link'] = item_link_lis
df.to_excel(filename+'.xlsx')

print('Finish')
