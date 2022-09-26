import pandas as pd

alunosDIC = {'Nomes':['Ricardo', 'Pedro', 'Roberto', 'Carlos'],
         'Nota':[4, 7, 5.5, 9],
         'Aprovado':['Não','Sim','Não','Sim']}

alunosDF = pd.DataFrame(alunosDIC)

# print(alunosDF)
# print(alunosDF['Nomes'])          #Mostra somente uma coluna com suas linhas.

# print(alunosDF.loc[[1, 2, 3]])        #Faz uma busca e mostra as linhas que você pedir. 
# print(alunosDF.loc[1:3])              #Funciona da mesma forma do fatiamento de string 0:2 :3  0, 1, 4.

# print(alunosDF.loc[ alunosDF['Nomes']=='Pedro' ])   #Faz uma busca de acordo com o que você pedir. Ex.: Buscar na coluna 'Nomes' o nome 'Pedro' e mostrar a linha desses nomes. 
print(alunosDF.loc[ alunosDF['Aprovado']=='Sim' ])