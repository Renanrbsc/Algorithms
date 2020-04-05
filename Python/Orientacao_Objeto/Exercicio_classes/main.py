from Orientacao_Objeto.Exercicio_classes.administrador import Administrador
from Orientacao_Objeto.Exercicio_classes.engenheiro import Engenheiro
from Orientacao_Objeto.Exercicio_classes.professor import Professor

professor_poo = Professor("Programação Orientada Objeto", "Noturno",
                          "Lucas", "Silva", 23, 40,
                          "Brasil", "Santa Catarina", "Blumenau", "Itoupavazinha", "Morro da Vila")
print(professor_poo)

engenheiro_dados = Engenheiro("Engenharia de dados", "Software para analise de dados",
                              "Renan", "Berti Ribas", 21, 40,
                              "Brasil", "Santa Catarina", "Blumenau", "Vila Nova", "Joinville")
print(engenheiro_dados)

administrador_dba = Administrador("Administração de Banco de Dados", "Analista de Suporte DBA",
                                  "Bruno", "Marcos", 27, 40,
                                  "Brasil", "Santa Catarina", "Florianopolis", "Bello", "Jose Lacerda")
print(administrador_dba)
