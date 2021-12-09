import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_page(page):
    headers = {'User-Agent': 'Use google to find steps for your browser user agent if needed. Helps to prevent scraper blocks'}
    url = f'https://www.indeed.com/jobs?q=python+developer&l=your_link_location_in_url={page}'
    r = requests.get(url, headers)
    grabber = BeautifulSoup(r.content, 'html.parser')
    return grabber
def get_posting(grabber):
    div_section = grabber.find_all('div', class_ = 'devs change the tags/classes update accordingly')
    for item in div_section:
        post_title = item.find('a').text.strip()
        post_company = item.find('span', class_ = 'devs change the tags/classes update accordingly').text.strip()
        print(post_company)
    

c = get_page(0)
get_posting(c)
    
