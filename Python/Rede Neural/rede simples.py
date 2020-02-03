from Pybrain.tools.shortcuts import buildNetwork
from Pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

ds = SupervisedDataSet(2,1)

ds.addSample((0.8, 0.4), (0.7))
ds.addSample((0.5, 0.7), (0.5))
ds.addSample((1.0, 0.8), (0.95))

nn = buildNetwork(2, 4, 1, bias=True)

trainer = BackpropTrainer(nn, ds)

for i in range(2000):
    print(trainer.train())

while True:
    dormiu = float(input("Dormiu quantas horas? "))
    estudou = float(input("Estudou quantas horas? "))
    
    z = nn.activate((dormiu, estudou))[0] * 10.0

    print(f"A previsão da nota será: {str(z)}")
    
