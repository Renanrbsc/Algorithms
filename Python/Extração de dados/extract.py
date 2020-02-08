from bs4 import BeautifulSoup
import requests

'''
# A biblioteca BeatifulSoup permite a construção de uma árvore
a partir de vários elementos de uma página HTML e fornece
uma simples interface para acessar estes elementos.
# A biblioteca requests é para realizar pedidos HTTP.
'''


class RatingLanguage:
    """Este algoritmo tem como intuito trazer uma lista com os dados em um ranking
    entre as linguagens mais utilizadas no ano passado e inicio de 2020"""

    def __init__(self):
        self.list_new = []

    def request(self):
        # Requisitando página HTML
        pag_html = requests.get("https://www.tiobe.com/tiobe-index/").text

        soup = BeautifulSoup(pag_html, 'html.parser')

        return soup
        # return soup.prettify()

    def scrapper_column_rows(self):
        """Nesta def será feito o tratamento
         de dados dos quais foram obtidos,
         teremos as colunas e linhas de uma tabela html"""

        soup = self.request()

        data_list = []
        for column in soup.find_all('td'):
            string = str(column)
            data = string.strip('</td>')
            data_list.append(data)

        return data_list

    def organizing_data(self):
        """Dados da primeira lista estao fora de ordem,
        criamos uma nova lista organizando os dados em indices de listas"""

        data_list = self.scrapper_column_rows()

        cont = 0
        list_a = []
        for i in data_list:
            if cont == 6:
                cont = 0
                self.list_new.append(list_a)
                list_a = []
            list_a.append(i)
            cont += 1
        return self.list_new

    def main(self):
        """Impressao de dados obtidos conforme indice da lista de 0 até 20
        Obtemos ranking de linguagens top20"""

        self.organizing_data()

        cont = 0
        for i in self.list_new:
            if cont == 20:
                break
            print(f"Jan 2020: {i[0]}\n"
                  f"Jan 2019: {i[1]}\n"
                  f"Change: {i[2]}\n"
                  f"Programming: {i[3]}\n"
                  f"Language: {i[4]}\n"
                  f"Ratings Change: {i[5]}\n")
            cont += 1


if __name__ == "__main__":
    ranking_language = RatingLanguage()
    ranking_language.main()
