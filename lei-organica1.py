import pandas as pd 
import re 
import requests 
from bs4 import BeautifulSoup 
import nltk 

# access the website 
page = requests.get('https://leismunicipais.com.br/lei-organica-cordeiro-rj')
html = page.text 
print (html) 

# import text from website into usable form 

# parse through text 

# extract desired text "atos administrativos de competência do Prefeito
