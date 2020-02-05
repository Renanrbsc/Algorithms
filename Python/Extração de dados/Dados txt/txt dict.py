
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

# for i in list_pokemon:
#     print(f'{i}'+'\n')


    



import MySQLdb

conexao = MySQLdb.connect(host = 'mysql.padawans.dev',
                          database = 'padawans16',
                          user = 'padawans16',
                          passwd = 'lr2019')

cursor = conexao.cursor()

def insert_pokemon_bd(cn,cr,lista):
    for i in lista:
        float_alt = float(i[3])
        float_pes = float(i[4])

        cr.execute(f"""INSERT INTO POKEMON
                (nome,tipo,altura,peso,categoria,habilidade,habilidade2,fraqueza,fraqueza2,descricao) 
            VALUES
                ('{i[1]}','{i[2]}',{float_alt},{float_pes},'{i[5]}','{i[6]}','{i[7]}','{i[8]}','{i[9]}','{i[10]}')""")
        print(f'Linha inserida: {i[0]} - ({i[1]},{i[2]},{float_alt},{float_pes},{i[5]},{i[6]},{i[7]},{i[8]},{i[9]},{i[10]})')
        cn.commit()

insert_pokemon_bd(conexao,cursor,list_pokemon)


    