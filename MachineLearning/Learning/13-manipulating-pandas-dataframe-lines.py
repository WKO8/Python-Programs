import pandas as pd

alunosDIC = {'Nomes':['Ricardo', 'Pedro', 'Roberto', 'Carlos'],
         'Nota':[4, 7, 5.5, 9],
         'Aprovado':['Não','Sim','Não','Sim']}

alunosDF = pd.DataFrame(alunosDIC)

# print(alunosDF)

primeiraslinhas = alunosDF.loc[0:2]         #Criando um novo DataFrame filtrando o DF anterior.
alunosDFbackup = alunosDF                   #Bom para salvar os dados para caso dê algo errado.

# print(primeiraslinhas)

novoDF = alunosDF.loc[alunosDF['Nota']!=9]      #Criando um novo DataFrame filtrando o DF principal com o .loc. 

# print(novoDF)

alunosReprovados = alunosDF.loc[alunosDF['Aprovado']!='Sim']

print(alunosReprovados)