import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# plt.scatter(x, y)
# plt.show()


# x1 = np.arange(0,1000,1)  #Cria um array que começa em 0 e vai até 999 de 1 em 1. 0,1,2,3...
# x1 = np.arange(-1000,1000,1)

# plt.plot(x1, -x1**2)
# plt.show()

#//Mostrar no gráfico a relação entre altura e peso do atletas masculinos do dataset das olimpíadas.

# Pegar o Dataset
dados = pd.read_csv('C:/Users/T-Gamer/Desktop/Meus Dados/Meus Dados/Programação/Programas Python/Machine Learning/athlete_events.csv')
# Filtrar somente os atletas masculinos
dadosMasc = dados.loc[dados['Sex']=='M']
# Buscar Altura e peso desses atletas
height = dadosMasc['Height']
weight = dadosMasc['Weight']
# Colocar no gráfico a altura e peso
plt.scatter(height, weight)
# Mostrar o gráfico
plt.show()
