
import requests

url = 'https://smarthistory.org/wp-json/smthstapi/v1/objects?tag=938&page={}'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
}

page_number = 1
while True:
    response = requests.get(url.format(page_number), headers=headers)
    data = response.json()

    print(response.url)
    # Do more with each page.

    if data.get('remaining') and int(data.get('remaining')) > 0:
        page_number += 1
    else:
        break