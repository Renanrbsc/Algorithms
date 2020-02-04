from bs4 import BeautifulSoup
import requests


#https://www.pokemon.com/br/pokedex

pag_html = requests.get("https://www.pokemon.com/br/pokedex/001").text

soup = BeautifulSoup(pag_html, 'html.parser')
print(soup.prettify())
