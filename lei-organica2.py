import pandas as pd 
import re 
import requests 
from bs4 import BeautifulSoup 
import nltk 


# access the website html 
url = 'https://leismunicipais.com.br/lei-organica-cordeiro-rj'
page = requests.get(url)
html = page.text 
# print (html) 


# define the regex pattern to detect and compile 
## multiline allows ^ and $ to match the start and end of lines in the pattern 
pattern = re.compile(r'^\s*(I|II|III|IV|V|VI|VII|VIII|IX|X)\s* -\s*.*$', re.MULTILINE) 


# find all the matches 
matches = pattern.findall(html) 


# print out the matched lines 
for match in matches: 
    print(match) 
print('done')
