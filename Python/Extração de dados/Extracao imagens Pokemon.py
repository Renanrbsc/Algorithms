import sys

sys.path.append(r"C:\Users\Usuario\Documents\GitHub\Desbravando-Algoritmos\Python\Extração de dados")

import requests
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

'''
# A biblioteca BeatifulSoup permite a construção de uma árvore
a partir de vários elementos de uma página HTML e fornece
uma simples interface para acessar estes elementos.
# A biblioteca requests é para realizar pedidos HTTP.
'''


class DataPokemons:
    """Extração de dados pagina Pokedex Pokemon
    https://www.pokemon.com/br/pokedex
    -- Script criado para obter dados dos pokemons e
    -- montar um banco de dados atraves do mesmo"""

    def __init__(self):
        self.pag_html = ''
        self.soup = None

    def request(self, j):
        self.pag_html = requests.get(f"https://www.pokemon.com/br/pokedex/{j}").text

        self.soup = BeautifulSoup(self.pag_html, 'html.parser')

        # return f"{self.soup.prettify()}"
        return self.soup

    # -- defs utilizadas para se obter dados especificos das tags
    # -- Utilizado metodo de extração por tags que continham class=""

    def title(self):
        """Obtendo Nome do Pokemon atraves da tag title do html"""

        title = str(self.soup.find_all("div", "pokedex-pokemon-pagination-title"))
        t = title.split('\n')
        t = str(t[2].strip(" "))
        return t

    def Imagens(self):
        """Obtendo Imagens dos Pokemon atraves da tag profile-images do html"""

        image = str(self.soup.find_all("div", "profile-images"))
        a = image.split('src="')
        a = str(a[1]).split('png"/>')
        a = str(a[0]) + 'png'
        return a

    def download_image(self, url_new, title):
        url = f"{url_new}"

        f = urllib.request.urlopen(url)
        data = f.read()
        with open(f"Images_pokemon\{title}.png", "wb") as code:
            code.write(data)

    def main(self):
        """Atraves dos dados obtidos podemos mostra-los na tela por ordem,
        Assim refazemos o processo em todas as paginas que contem dados e
        salvamos em um txt"""

        # -- Loop de requests para obter dados das paginas necessarias
        for j in range(1, 3):
            self.request(j)
            url_new = self.Imagens()
            self.download_image(url_new, self.title())

            # -- Exibindo na tela valores obtidos
            print(f'-----Pokemon Image Code: {j}-----')
            print(url_new)
            print(f'----------------------------')


if __name__ == "__main__":
    pokedex = DataPokemons()
    pokedex.main()
