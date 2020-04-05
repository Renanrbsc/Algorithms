from Orientacao_Objeto.Herança_de_classe.cliente import Cliente
from Orientacao_Objeto.Herança_de_classe.funcionario import Funcionario


cliente1 = Cliente('Renan', 'Berti', 21, '256325412', 1250.00)
cliente1.mostrar_dados()

cliente2 = Cliente('Luiz', 'Silva', 16, '458745874', 741.00)
cliente2.mostrar_dados()

funcionario1 = Funcionario('Renan', 'Berti', 21, '256325412', 'HBSIS')
funcionario1.mostrar_dados()

funcionario2 = Funcionario('Luiz', 'Silva', 16, '458745874', 'Padaria do Zé')
funcionario2.mostrar_dados()
