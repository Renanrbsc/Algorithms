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

data_list = []
for column in soup.find_all('td'): # Busca as colunas da tabela html
    string = str(column) # converte o indice de formato 'bs4' em string
    data = string.strip('</td>') # retira caracters da string
    data_list.append(data) # adiciona o dado em uma lista

print(data_list)

cont=0
list_a = [] 
list_b = []       
for i in data_list:
    if cont == 6:
        cont = 0
        list_b.append(list_a)
        list_a = []
    list_a.append(i)
    cont += 1

cont=0
for i in list_b:
    if cont == 20:
        break
    print(f'Jan 2020: {i[0]}    Jan 2019: {i[1]}    Change: {i[2]}    Programming: {i[3]}    Language: {i[4]}    Ratings Change: {i[5]}')
    cont+=1
    

