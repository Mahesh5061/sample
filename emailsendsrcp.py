from bs4 import BeautifulSoup as btfs
import requests
import smtplib

re = requests.get('https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html')
res = re.content

soup = btfs(res,'html.parser')
price = float(soup.find('p', class_='price_color').text[1:])
print(price)

if(price<60):
    smt = smtplib.SMTP('smtp.gmail.com', 587)
    smt.ehlo()
    smt.starttls()
    smt.login('maheshkalaga535@gmail.com','czht btrb uyuw eryt')
    smt.sendmail('maheshkalaga535@gmail.com','dhineshk1702@gmail.com',
                 f"subject:Head phones price \n\n Hi price {price} Buy it" )
    smt.quit()
