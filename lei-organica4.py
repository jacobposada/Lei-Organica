import pandas as pd 
import re 
import requests 
from bs4 import BeautifulSoup 

# website list 
district_statuses = '/Users/jacobposada/columbia/econ research/Lei-Organica/leis_organicas_scraping_status.xlsx' 
df = pd.read_excel(district_statuses, 'Sheet1')

# change excel sheet to list of dictionaries 
district_sites = df.to_dict(orient='records')

# database to store in 
law_sections = [] 


def parse_html(site): 
    # parses through html text from the Website column of a site file 

    url = 'https://leismunicipais.com.br/' + site['city_code']
    print(url) 
    page = requests.get(url) 
    html = page.text 
    return html 

def extract_district_name(soup: str) -> str: 
    # extracts name of district from each site 

    # pattern to detect, only captures "Municipio de ...."
    pattern = re.compile(r'<title>Lei Orgânica de (.*?)</title>', re.DOTALL)
        # pattern = re.compile(r'<h[0-9]>LEI ORGÂNICA DO (.*?).</h[0-9]>', re.DOTALL) 

    # find matches 
    header_text = pattern.search(soup) 

    if header_text == None: 
        pattern = re.compile(r'<title>Leis de (.*?)</title>', re.DOTALL) 
        header_text = pattern.search(soup) 

    return header_text.group(1) 


def extract_relevant_text(soup: str) -> str:
    # extracts the law text from the HTML

    # find beginning of text to extract 
    try: 
        match = re.search(r'atos administrativos de competência do Prefeito(.*?) I -', soup)
        initial_index = match.end() - 3
    except: 
        match = re.search(r'atos administrativos de competência do Prefeito(.*?).', soup)
        initial_index = match.end() 

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

    # split text into sections based on roman numerals or numbers 
    try: 
        section_split = re.split(r'(?<!\S)(?=[IVXLCDM]+ - \b)', text) 
    except: 
        section_split = re.split(r'(?<!\S)(?=[0-9]+. \b)')
    section_split = [section.strip() for section in section_split if section.strip()]

    # extract subsections for each section 
    for section in section_split: 

        # extract roman numeral 
        section_numeral = section[:section.index(' ')] 

        # section content string 
        try: 
            section_content = section[section.index('- '):section.index(' a)')] 
        except: 
            semicolon_index = section.find(';') 
            period_index = section.find('. ') 
            if semicolon_index != -1: 
                end_index = semicolon_index 
            else: 
                end_index = period_index 
            section_content = section[section.index('- '):end_index] 
        
        # isolate all the subsections 
        subsections = re.findall(r'([a-z]\) (.+?)(?=[a-z]\)|$))', section) 

        # append to law_sections the roman numeral and subsection combinations 
        for subsection in subsections: 
            subsec_letter, subsec_content = subsection 
            subsec_letter = subsec_letter[:1]
            law_sections.append({'District Name': None,'Section Number': section_numeral, 'Section Content': section_content, 'Subsection Letter': subsec_letter, 'Subsection Content': subsec_content}) 
    
    return law_sections  


# go through each website 
    # cycle through district sites 
for site in district_sites: 
    if site['status'] == 'success': 
            # parse html code 
            html = parse_html(site) 
            
            # extract relevant text 
            try: 
                section_of_interest = extract_relevant_text(html) 

                # format data 
                extracted_data = extract_data(section_of_interest) 
            
            except: 
                law_sections.append({'District Name': None, 'Section Number': 'Error: No data found on website', 'Section Content': None, 'Subsection Letter': None, 'Subsection Content': None})
            
            # extract district name 
            dist_name = extract_district_name(html) 
            
            # append district name data to total data 
            site['District Name'] = dist_name 


# create pandas dataframe 
laws_df = pd.DataFrame(law_sections) 
laws_df.to_excel('laws_data.xlsx') 