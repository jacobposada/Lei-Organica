import pandas as pd 
import re 
import requests 
from bs4 import BeautifulSoup 
import nltk 

# access the website 
url = 'https://leismunicipais.com.br/lei-organica-cordeiro-rj'
page = requests.get(url)
html = page.text 
# print (html) 

# parse through text 
pattern = re.compile(r'atos administrativos de competência do Prefeito') 
matches = pattern.findall(html)

# extract desired text "atos administrativos de competência do Prefeito" 
for match in matches: 
    print(match) 
