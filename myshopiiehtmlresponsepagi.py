import math

import requests
from bs4 import BeautifulSoup


index_page = 'https://techinstr.myshopify.com/collections/all'
url = 'https://techinstr.myshopify.com/collections/all?page={}'

session = requests.session()
response = session.get(index_page)
soup = BeautifulSoup(response.text, "lxml")
count_element = soup.select_one('.filters-toolbar__product-count')
count_str = count_element.text.replace('products', '')
total_count = int(count_str)
# Do more with the first page.

page_count = math.ceil(total_count/8)
for page_number in range(2, page_count+1):
    response = session.get(url.format(page_number))
    soup = BeautifulSoup(response.text, "lxml")
    first_product = soup.select_one('.product-card:nth-child(1) > a > span')
    print(first_product.text.strip())
    # Do more with each of the pages.