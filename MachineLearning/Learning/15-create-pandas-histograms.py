import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/T-Gamer/Desktop/Meus Dados/Meus Dados/Programação/Programas Python/Machine Learning/athlete_events.csv')

dados.hist(column='Weight', bins=100)   # column = 'Coluna que vc qr fazer o histograma'  
                                        # bins = Número de barras no gráfico.
                                        # Cálculo do histograma: 
                                        # Diferença entre as idades e dividir pelo número de caixas(bins)
                                        # Idades = 10 a 90 anos -> 90-10 = 80
                                        # Caixas = 100
                                        # 80/100 = 0.8
                                        # Logo, o comprimento de cada caixa será de 0.8

plt.show()

# plt.hist(nome_array, bins=100)  # Fazer histograma com array.