
# -- Criação de uma lista com dados do arquivo txt
# -- lançamento de codigo em cada sublista

list_pokemon = []
with open('Desbravando-Algoritmos\Python\Extração de dados\Dados txt\dados_pokemon.txt', encoding = 'utf-8') as arq:
    i = 1
    for dados in arq:
        list_cont = []
        dados.strip()
        list_dados = dados.split(';')
        list_cont.append(i)
        for j in list_dados:
            a = str(j).replace('\n','')
            list_cont.append(a)
        list_pokemon.append(list_cont)
        i += 1

for i in list_pokemon:
    print(f'{i}'+'\n')

    