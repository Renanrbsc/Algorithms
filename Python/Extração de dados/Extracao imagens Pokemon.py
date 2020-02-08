from bs4 import BeautifulSoup
import requests
import urllib.request, urllib.parse, urllib.error

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
        self.url = ''

    def request(self, j):
        self.pag_html = requests.get(f"https://www.pokemon.com/br/pokedex/{j}").text

        self.soup = BeautifulSoup(self.pag_html, 'html.parser')

        # return f"{self.soup.prettify()}"
        return self.soup

    # -- defs utilizadas para se obter dados especificos das tags
    # -- Utilizado metodo de extração por tags que continham class=""

    def Imagens(self):
        """Obtendo Imagens dos Pokemon atraves da tag profile-images do html"""

        list_image = []

        image = str(self.soup.find_all("div", "profile-images"))
        a = image.split('src="')
        a = str(a[1]).replace('"/>','')
        a = str(a).replace('</div>]','')
        a = str(a).replace('\n','')
             
        return a

    def download_image(self, url_new, j):
        self.url = f"{url_new}"
          
        print("baixando com urllib2")
        f = urllib.request.urlopen(self.url)
        data = f.read()
        with open(f"Desbravando-Algoritmos\Python\Extração de dados\Images\{str(j)}.png", "wb") as code:
            code.write(data)

    def main(self):
        """Atraves dos dados obtidos podemos mostra-los na tela por ordem,
        Assim refazemos o processo em todas as paginas que contem dados e
        salvamos em um txt"""

        # -- Loop de requests para obter dados das paginas necessarias
        for j in range(1, 810):

            self.request(j)
            url_new = self.Imagens()
            self.download_image(url_new, j)
            
            # -- Exibindo na tela valores obtidos
            print(f'-----Pokemon Image Code: {j}-----')
                print(url_new)
            print(f'----------------------------')


if __name__ == "__main__":
    pokedex = DataPokemons()
    pokedex.main()
