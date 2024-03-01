import pandas as pd 
import re 
import requests 
from bs4 import BeautifulSoup 
import csv 

# website list 
district_sites_csv = '/Users/jacobposada/columbia/econ research/district_sites.csv'




def parse_html(site): 
    # parses through html text from the Website column of a site file 

    url = site['Website'] 
    page = requests.get(url) 
    html = page.text 
    return html 

def extract_district_name(soup: str) -> str: 
    # extracts name of district from each site 

    # pattern to detect, only captures "Municipio de ...."
    pattern = re.compile(r'<h1>LEI ORGÂNICA DO (.*?).</h1>', re.DOTALL)

    # find matches 
    header_text = pattern.search(soup) 

    return header_text.group(1) 


def extract_relevant_text(soup: str) -> str:
    # extracts the law text from the HTML

    # find beginning of text to extract
    initial_index = re.search("atos administrativos de competência do Prefeito", soup).end()

    # storing the remaining text
    remaining_text = soup[initial_index:]

    # obtaining final index
    final_index = re.search("artigo", remaining_text).start()

    # updating remaining text
    law_text = remaining_text[:final_index]

    return law_text
    

def extract_data(html_string): 
    # separates and formats data 

    # parse html 
    soup = BeautifulSoup(html_string, 'html.parser')

    # extract text from html 
    text = soup.get_text() 

    # split text into sections based on roman numerals 
    section_split = re.split(r'\b(?=[IVXLCDM]+\b)', text) 
    section_split = [section.strip() for section in section_split if section.strip()]

    # extract subsections for each section 
    law_sections = []
    for section in section_split: 

        # extract roman numeral 
        section_numeral = section[:section.index(' ')] 

        # roman numeral string 
        section_content = section[section.index(' ')+3:section.index(':')]
        
        # isolate all the subsections 
        subsections = re.findall(r'([a-z]\) (.+?)(?=[a-z]\)|$))', section) 

        # append to law_sections the roman numeral and subsection combinations 
        for subsection in subsections: 
            subsec_letter, subsec_content = subsection 
            subsec_letter = subsec_letter[:1]
            law_sections.append({'District Name': None,'Section Number': section_numeral, 'Section Content': section_content, 'Subsection Letter': subsec_letter, 'Subsection Content': subsec_content}) 
    
    return law_sections  


# go through each website 
with open(district_sites_csv, newline='') as csvfile: 
    dist_sites = csv.DictReader(csvfile) 

    # cycle through district sites 
    for site in dist_sites: 
        
        # parse html code 
        html = parse_html(site) 

        # extract relevant text 
        section_of_interest = extract_relevant_text(html) 

        # extract district name 
        dist_name = extract_district_name(html) 

        # format data 
        extracted_data = extract_data(section_of_interest) 

        # append district name data to total data 
        for entry in extracted_data: 
            entry['District Name'] = dist_name 


# create pandas dataframe 
laws_df = pd.DataFrame(extracted_data) 
laws_df.to_excel('laws_data.xlsx') 