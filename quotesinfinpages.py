import requests

url = 'http://quotes.toscrape.com/api/quotes?page={}'
page_number = 1
while True:
    response = requests.get(url.format(page_number))

    # Do more with each page.
    data = response.json()
    print(response.url)
    for quote in data['quotes']:
        print(quote['text'])
    if data.get('has_next'):
        page_number += 1
    else:
        break