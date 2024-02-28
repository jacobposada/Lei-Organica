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


def extract_law_text(soup: str) -> str:
    
    # extracts the law text from the HTML

    try:
        # find beginning of text to extract
        initial_index = re.search("atos administrativos de competência do Prefeito", soup).end()

        # storing the remaining text
        remaining_text = soup[initial_index:]

        # obtaining final index
        final_index = re.search("artigo", remaining_text).start()

        # updating remaining text
        remaining_text = remaining_text[:final_index]

        return remaining_text
    
    except:
        return None


def extract_data(html_string): 

    # parse html 
    soup = BeautifulSoup(html_string, 'html.parser')

    # extract text from html 
    text = soup.get_text() 

    # split text into sections 
    section_split = re.split(r'\b(?=[IVXLCDM]+\b)', text) 
    section_split = [section.strip() for section in section_split if section.strip()]

    # extract subsections for each section 
    law_sections = []
    for section in section_split: 

        # extract roman numeral 
        section_numeral = section[:section.index(' ')] 

        # roman numeral string 
        section_content = section[section.index(' '):section.index(': )')]
        
        # isolate all the subsections 
        subsections = re.findall(r'([a-z]\) (.*?) (?=[a-z]+\)))', section, re.IGNORECASE) 

        # append to law_sections the roman numeral and subsection combinations 
        for subsection in subsections: 
            subsection_letter = subsection[:subsection.index(')')] 
            subsection_content = subsection[subsection.index(')'):subsection.index(':')]
            law_sections.append({'Section Number': section_numeral, 'Section Content': section_content, 'Subsection Letter': subsection_letter, 'Subsection Content': subsection_content}) 
    
    return law_sections  


# print out the matched lines 
section_of_interest = extract_law_text(html) 
extracted_data = extract_data(section_of_interest) 
#print(extracted_data) 

# create pandas dataframe 
laws_df = pd.DataFrame(extracted_data) 
print(laws_df) 
laws_df.to_excel('laws_data.xlsx') 