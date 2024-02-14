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

# define the regex pattern to detect 
pattern = r'^\s*(I|II|III|IV|V|VI|VII|VIII|IX|X)\s*-\s*.*$' 

# compile the regex pattern 
## multiline allows ^ and $ to match the start and end of lines in the pattern 
regex = re.compile(pattern, re.MULTILINE) 

# find all the matches 
matches = regex.findall(html) 

# print out the matched lines 
for match in matches: 
    print(match) 
    print('done')
