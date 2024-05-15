"""Handling pages with the Next button"""
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

url = 'https://sandbox.oxylabs.io/products'

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    page_number = soup.select_one('li.active > a')
    print(page_number['aria-label'])
    # Do more with each page.

    # Find the next page to scrape in the pagination.
    next_page_element = soup.select_one('li.next > a')

    next_page_url = next_page_element.get('href')
    if (next_page_url == '#'):
        break
    url = urljoin(url, next_page_url)