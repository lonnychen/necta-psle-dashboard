#webscraping.py

####################
#Libraries
#Webscraping
import requests
from requests.adapters import HTTPAdapter, Retry
from time import sleep
from bs4 import BeautifulSoup
#Strings
import re
#Custom modules
from config import base_URL
####################

def session_retries(URL: str, timeout: int=10, retries: int=10):
    '''Use "Session" retries in case webpage times out'''
    s = requests.Session()
    r = Retry(total=retries, backoff_factor=1)
    s.mount('https://', HTTPAdapter(max_retries=r))  
    while True:
        try:
            response = s.get(URL, timeout=timeout)
            with open('../debug/http_responses.txt', 'a') as f:
                f.write(f"{URL} {response.status_code} {response.reason}\n")
            break
        except requests.exceptions.ConnectionError as error:
            with open('../debug/http_responses.txt', 'a') as f:
                f.write(f"{URL} {response.status_code} {response.reason} {error}\nSleeping for 10 seconds...\n")
            sleep(10)
            continue
    return response

def school_scrape(URL: str, is_retries: bool=False):
    '''Webscrapes primary school examination results from each school's web page
    Parameters:
        URL (str): school web page to scrape
        is_retries (bool): whether to use "Session" retires
    Returns:
        Raw unprocessed page data (dict)
    '''
    if is_retries:
        #DEBUG: needed for national dataset
        response = session_retries(URL) 
    else:
        response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    #Initialize page data dictionary
    page = {'results_url': URL}
    
    #(i) Find/regex school information
    school = soup.find('h3').get_text(strip=True)
    m = re.search('(.*\S)\s*(PRIMARY SCHOOL|SEMINARY)\W+(\w+)', school)
    if (m != None): #In case of missing data
        page['school_name'] = m[1].upper() #match TAMISEMI uppercase names
        page['school_id'] = m[3]

    #(ii) Find/regex school overall results
    results = soup.find('font').get_text(strip=True)
    m = re.search('WALIOFANYA MTIHANI\D*(\d+)\s*WASTANI WA SHULE\D*([\d.]+)\s*DARAJA\W+(\w)', results)
    if (m != None): #In case of missing data
        page['num_sitters'] = int(m[1]) #number of students who "sat for exam"
        page['average_300'] = float(m[2]) #PSLE average score out of 300 max
        page['grade'] = m[3] #A-E grade

    #(iii) Find/regex gender x grade results
    grades = soup.find_all('tr', limit=4) #WORKAROUND for a broken first table
    for tr in grades[1:]: #rows
        for i, td in enumerate(tr.find_all('td')): #column-data
            if i == 0: #index column of row
                idx = td.get_text(strip=True)
                page[idx] = []
            else:
                page[idx].append(int(td.get_text(strip=True)))
    
    return page

def council_scrape(URL: str, region_name, council_name):
    '''Webscrapes council web page for list of school web pages to scrape
    Parameters:
        URL (str): council web page to scrape
        region_name (str): passed from nation scrape
        council_name (str): passed from region scrape
    Returns:
        List of school page data (list of dicts)
    '''
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    data = list()

    schools = soup.find_all('a')
    for s in schools:
        school_URL = base_URL + 'results/' + s['href']
        #School level scrape in function > returns dict of school data
        page = school_scrape(school_URL, True)
        #Add supplemental info from higher pages
        page['region_name'] = region_name
        page['council_name'] = council_name
        #Add to list of schools
        data.append(page)

    return data

def region_scrape(URL: str, region_name):
    '''Webscrapes region web page for list of council web pages to scrape
    Parameters:
        URL (str): region web page to scrape
        region_name (str): passed from nation scrape
    Returns:
        List of school page data (list of dicts)
    '''
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    data = list()
    
    councils = soup.find_all('a')
    for c in councils:    
        council_name = c.get_text(strip=True).capitalize() #match TAMISEMI
        m = re.search('(.*)\s+(\w{2})', council_name) #e.g., handle 'MOROGORO MC' > 'Morogoro MC'
        if m != None: council_name = f"{m[1]} {m[2].upper()}" 
        council_URL = base_URL + 'results/' + c['href']
        data += council_scrape(council_URL, region_name, council_name)
        
    return data

def nation_scrape(URL: str):
    '''Webscrapes region web page for list of council web pages to scrape
    Parameters:
        URL (str): region web page to scrape
        region_name (str): passed from nation scrape
    Returns:
        List of school page data (list of dicts)
    '''
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    data = list()

    regions = soup.find_all('a') #just find all hyperlink tags!
    for r in regions:
        region_name = r.get_text(strip=True).capitalize() #match TAMISEMI
        region_URL = base_URL + r['href']
        data += region_scrape(region_URL, region_name)
    
    return data
