import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/T-Gamer/Desktop/Meus Dados/Meus Dados/Programação/Programas Python/Machine Learning/athlete_events.csv')

dados.boxplot(column=['Age', 'Height', 'Weight'])     #pandas 
plt.show()                      #matplotlib