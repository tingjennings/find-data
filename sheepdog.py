import os
from splinter import Browser, browser
from bs4 import BeautifulSoup 
import requests
import pandas as pd
from splinter.exceptions import ElementDoesNotExist
from webdriver_manager.chrome import ChromeDriverManager
url = "https://sheepdogresponse.com/collections/live-training"
executable_path = {'executable_path': 'c:/Webdrivers/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)  
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
html[:60]

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
contents = soup.find_all('a', class_='boost-pfs-filter-product-item-title')

f = open("result2.txt", "w", encoding="utf-8")
for content in contents:
   f.write(content.string)
print(content.string)

f.close()
