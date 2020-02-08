from bs4 import BeautifulSoup
import requests

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

    def type_pokemon(self):
        """Obtendo Tipo do Pokemon atraves da tag type do html"""

        type_pokemon = self.soup.find_all("div", "dtm-type")
        h = str(type_pokemon).split('>')
        h = h[6].strip('</a')
        return h

    def attribute(self):
        """Obtendo Atributos do Pokemon atraves da tag de tabela do html"""

        list_attribute = []

        attribute = self.soup.find_all("span", "attribute-value")
        # -- Altura
        h = str(attribute[0]).strip(' m</span class="attribute-value">')
        list_attribute.append(h)
        # -- Peso
        h = str(attribute[1]).strip(' kg</span class="attribute-value">')
        list_attribute.append(h)
        # -- Categoria
        h = str(attribute[3]).replace('<span class="attribute-value">', '')
        h = h.replace('</span>', '')
        list_attribute.append(h)
        # -- Habilidade Principal
        if len(attribute) >= 5:
            h = str(attribute[4]).replace('<span class="attribute-value">', '')
            h = h.replace('</span>', '')
            list_attribute.append(h)
        else:
            h = ''
            list_attribute.append(h)
        # -- Habilidade Secundaria
        if len(attribute) == 6:
            h = str(attribute[5]).replace('<span class="attribute-value">', '')
            h = h.replace('</span>', '')
            list_attribute.append(h)
        else:
            h = ''
            list_attribute.append(h)

        return list_attribute

    def weakness(self):
        """Obtendo Fraquezas do Pokemon atraves da tag weaknesses do html"""

        list_weakness = []

        weakness = str(self.soup.find_all("div", "dtm-weaknesses"))
        a = str(weakness).split('<span>')
        # -- Fraqueza
        h = str(a[1]).split('\n\t')
        h = h[0]
        list_weakness.append(h)
        # -- Fraqueza 2
        if len(a) >= 3:
            t = str(a[2]).split('\n\t')
            t = t[0]
            list_weakness.append(t)
        else:
            t = ''
            list_weakness.append(t)

        return list_weakness

    def description(self):
        """Obtendo Descrição do Pokemon atraves da tag version-y do html"""

        description = str(self.soup.find_all("p", "version-y"))
        desc = description.split('                  ')
        desc = desc[1].split('\n ')
        desc = desc[0].replace('\n', '')
        return desc

    def main(self):
        """Atraves dos dados obtidos podemos mostra-los na tela por ordem,
        Assim refazemos o processo em todas as paginas que contem dados e
        salvamos em um txt"""

        # -- Loop de requests para obter dados das paginas necessarias
        for j in range(1, 810):
            dados_pokemon = []

            self.request(j)

            dados_pokemon.append(self.title())
            dados_pokemon.append(self.type_pokemon())

            for at in self.attribute():
                dados_pokemon.append(at)

            for we in self.weakness():
                dados_pokemon.append(we)

            dados_pokemon.append(self.description())

            # -- Exibindo na tela valores obtidos
            print(f'-----Pokemon Code: {j}-----')
            for i in dados_pokemon:
                print(i)
            print(f'----------------------------')

            # -- salvando dados obtidos para Database
            arq = open('dados_pokemon.txt', 'a', encoding='utf-8')
            arq.write(';'.join(dados_pokemon) + '\n')
            arq.close()


if __name__ == "__main__":
    pokedex = DataPokemons()
    pokedex.main()
