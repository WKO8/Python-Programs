import pandas as pd
dados = pd.read_csv('C:/Users/T-Gamer/Desktop/Meus Dados/Meus Dados/Programação/Programas Python/Machine Learning/athlete_events.csv')

# print(dados.head())

dados.drop('ID', axis = 1, inplace=True)        # axis = 1 -> coluna
dados.drop(0, axis = 0, inplace=True)    # axis = 0 -> linha
dados.drop('City', axis = 1, inplace=True)      # inplace = True -> Continuar na mesma linha

print(dados.head())