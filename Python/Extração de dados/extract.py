from bs4 import BeautifulSoup
import requests

'''
# A biblioteca BeatifulSoup permite a construção de uma árvore
a partir de vários elementos de uma página HTML e fornece
uma simples interface para acessar estes elementos.
# A biblioteca requests é para realizar pedidos HTTP.
'''

# Requisitando página HTML
pag_html = requests.get("https://www.tiobe.com/tiobe-index/").text

# 
soup = BeautifulSoup(pag_html, 'html.parser')
# print(soup.prettify())

# ------- Obtendo os valores de linhas e colunas --------

# for rows in soup.find_all('tr'):
for column in soup.find_all('td'):
    # print(column)
    print(column.prettify())
    # for data in soup.get('td'):
    #     print(data)

