import os
from splinter import Browser, browser
from bs4 import BeautifulSoup 
import requests
import pandas as pd
from splinter.exceptions import ElementDoesNotExist
from webdriver_manager.chrome import ChromeDriverManager
url = "https://fieldcraftsurvival.com/training/"
executable_path = {'executable_path': 'c:/Webdrivers/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)  
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
html[:60]

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
contents = soup.find_all('h3')

f = open("fieldcraftsurvival result.txt", "w", encoding="utf-8")
for content in contents:
  if (content.a != None):
     f.write(content.a.get('aria-label'))

f.close()
