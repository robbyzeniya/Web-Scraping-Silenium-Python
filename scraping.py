from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

#path driver chromium
PATH = "D:\Robby\Project\scrapping\chromedriver.exe" #deklarasi path cromium 
driver = webdriver.Chrome() #Eksekusi file chromium

driver.get("https://www.accuweather.com/")

#Ambil title
print(driver.title)

#search untuk nama cuaca indonesia, contoh : Jakarta, Surabaya
search = driver.find_element_by_xpath("//input[@name='query' and @class='search-input']") #Cari element search
search.send_keys("Jakarta, Indonesia") #masukan value test 
search.send_keys(Keys.RETURN) #eksekusi 

#saat page diload, tunggu maks 40 detik sampai halaman berhasil di load
try:
    WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.ID, "base-header"))
    )
finally:
    #get cuaca
    headers = driver.find_elements_by_xpath("//p[@class='module-header']")
    header = [x.text for x in headers]
    #jika ditemukan hasil cuaca?
    if(header):
        print('CUACA :')
        print(header, '\n')
        #get temperatur
        temparatures = driver.find_elements_by_xpath("//div[@class='temp']")

        temparature = [x.text for x in temparatures]

        print("Temperature:")
        print(temparature, '\n')

        for xz, yz in zip(header, temparature):
            print("Hari : Temparature")
            print(xz + ": " + yz, '\n')
    else:
        #jika tidak ditemukan
        list_element_citys = driver.find_elements_by_xpath("//div[@class='search-results']")
        list_element_city = [x.text for x in list_element_citys]
        print("Result City:")
        print(list_element_citys, '\n')


