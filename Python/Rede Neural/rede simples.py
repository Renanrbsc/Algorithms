from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

# -- Biblioteca pybrain com codigo fonte mantido no github
# -- Possibilita o Aprendizado da maquina apartir de exemplos
# -- Neste algoritmo é passado 3 parametros para serem processados nos neuronios
# -- Para o valor de saida é necessario que haja duas entradas, sendo elas
# -- "Quantas horas o aluno dormiu" e "Quantas horas o aluno estudou"
# -- e a saida sendo "Previsão de nota obtida"

# -- Entrada e saida para os neuronios
ds = SupervisedDataSet(2,1)

# -- Exemplos
ds.addSample((0.8, 0.4), (0.7))
ds.addSample((0.5, 0.7), (0.5))
ds.addSample((1.0, 0.8), (0.95))

# -- Construção dos neuronios (entradas, ligaçoes, saida)
nn = buildNetwork(2, 4, 1, bias=True)

# -- Instancia do metodo para treina-lo
trainer = BackpropTrainer(nn, ds)

# -- Loop de treino para a Rede Neural
for i in range(2000):
    print(trainer.train())

# -- Solicitando parametros para a rede após treinada
while True:
    dormiu = float(input("Dormiu quantas horas? "))
    estudou = float(input("Estudou quantas horas? "))
    
    z = nn.activate((dormiu, estudou))[0] * 10.0

    print(f"A previsão da nota será: {str(z)}")
    
