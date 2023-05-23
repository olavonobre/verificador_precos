import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.es/-/pt/dp/B08KKJ37F7/ref=sr_1_3?crid=1CDYI19T5AQXX&keywords=ps5&qid=1684872390&sprefix=ps5%2Caps%2C95&sr=8-3'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36" }

site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

title = soup.find('span', class_ = 'a-size-large product-title-word-break').get_text().strip()
price = soup.find('span', class_ = 'a-price-whole').get_text()


print('O seu', title , 'esta custando', price)

