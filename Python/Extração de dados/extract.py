from bs4 import BeautifulSoup
import requests
import  matplotlib.pyplot as plt

'''
A biblioteca BeatifulSoup permite a consrução de uma árvore a partir de vários elementos de uma página HTML
e fornece uma simples interface para acessar estes elementos.
A biblioteca requests é para realizar pedidos HTTP. 
A biblioteca matplotlib é para a construção de gráficos 2D para visualizar melhor os nossos dados.
'''


# Requisitando página HTML (Frota ano de 2003 - Blumenau SC -- DETRAN/SC)
'''
A requisiçao desta URL retorna uma página HTML com os dados em tabelas, linhas e colunas referentes a quantidade
de frotas de veículos na cidade de Blumenau ano de 2003.
** Neste programa o dado de interesse é a quantidade de AUTOMOVEIS 
'''
pagina_html = requests.get("https://www.facebook.com/search/people/?q=Amanda&epa=SERP_TAB").text

# soup = BeautifulSoup(pagina_html, 'html5lib')
soup = BeautifulSoup(pagina_html, 'html.parser')
#print(soup.prettify())

# ------- Tratamento dos dados e obtendo os valores --------
links = soup.find_all('a')

for link in soup.find_all('a'):
    print(link.get('href'))
