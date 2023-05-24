import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.es/-/pt/dp/B08KKJ37F7/ref=sr_1_3?crid=1CDYI19T5AQXX&keywords=ps5&qid=1684872390&sprefix=ps5%2Caps%2C95&sr=8-3' #site da Amazon com o produto playstation 5

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36" } #mecanismos que os sites usam dos nossos navegadores

site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser') #usando o beautifulSoup para todo o site e guardar em soup


#Usei o soup.find para localiza uma determiada linha/posição dentro do codigoo html (span com classe 'a-size-large product-title-word-break')
#e salvei dentro de title ( NESTE CASO O TÍTULO DO PRODUTO)
title = soup.find('span', class_ = 'a-size-large product-title-word-break').get_text().strip() 

#USEI NOVAMENTE O soup.find para desta vex buscar o valor deste produto
price = soup.find('span', class_ = 'a-price-whole').get_text()

#aqui imprimi o titulo e o valor
print('O seu', title , 'esta custando', price)

#Agora é implementar busca de variacoes desse preco

