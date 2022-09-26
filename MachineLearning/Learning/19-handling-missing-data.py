import pandas as pd
dados = pd.read_csv('C:/Users/T-Gamer/Desktop/Meus Dados/Meus Dados/Programação/Programas Python/Machine Learning/athlete_events.csv')

dados2 = dados.dropna()  # Exclui todos as linhas que possuem dados faltantes (NaN) do DataSet.

enulo = dados.isnull()   # Recebe todo os dados e altera-os para True ou False, para caso falte ou não dados.

faltantes = dados.isnull().sum()  # Soma todos os valores positivos de cada coluna e coloca ao lado da coluna esse número.

faltantes_percentual = (dados.isnull().sum() / len(dados['ID']))*100    # Pega todos os dados nulos de cada coluna e divide pelo número de linhas
                                                                        # do DataSet, calculando o percentual de dados faltantes de cada coluna.

dados['Medal'].fillna('Nenhuma', inplace=True)     # Preenche os dados faltante por alguma coisa, no caso "Nenhuma"
                                                   # inplace=True -> Substitui no mesmo lugar que estava o dado anterior.    
                 
dados['Age'].fillna(dados['Age'].mean(), inplace=True) # Preenche os dados faltante pela média de todos os dados. (idade no caso)
dados['Height'].fillna(dados['Height'].mean(), inplace=True) # Preenche os dados faltante pela média de todos os dados. (idade no caso)
dados['Weight'].fillna(dados['Weight'].mean(), inplace=True) # Preenche os dados faltante pela média de todos os dados. (idade no caso)

faltantes_percentual = (dados.isnull().sum() / len(dados['ID']))*100
print(faltantes_percentual)