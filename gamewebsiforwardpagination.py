"""Handling pages without the Next button"""
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

# Get the first page.
url = 'https://sandbox.oxylabs.io/products'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
page_link_el = soup.select('.pagination a')
index_page = page_link_el[0].get('href')

last_page = page_link_el[len(page_link_el)-2].get('href')
last_page_number = str(last_page)[-2:]

# Make links for and process the following pages.
for i in range (1,int(last_page_number)):
   link = urljoin(url, "products?page=" + str(i) )
   response = requests.get(link)
   soup = BeautifulSoup(response.text, 'lxml')
   print(response.url)
   # Do more with each page.