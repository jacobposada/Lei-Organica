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
pattern = re.compile(r'([IVXLCDM]+ - .*?)<', re.MULTILINE) 


# find all the matches 
matches = pattern.findall(html) 


# create pandas dataframe 
laws_df = pd.DataFrame(matches, columns=['Match'])


# print out the matched lines 
print (laws_df) 
# for match in matches: 
    # print("Match:", match) 
# print('end')

