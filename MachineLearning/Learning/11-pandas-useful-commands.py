import pandas as pd

alunosDIC = {'Nomes':['Ricardo', 'Pedro', 'Roberto', 'Carlos'],
         'Nota':[4, 7, 5.5, 9],
         'Aprovado':['Não','Sim','Não','Sim']}

alunosDF = pd.DataFrame(alunosDIC)

# print(alunosDF.head())        #Mostra o DataFrame com o cabeçalho (de forma mais completa).
# print(alunosDF.shape)         #Mostra o tamanho do DataFrame
print(alunosDF.describe())    #Mostra cálculos matemáticos com os dados. Ex.: Média, min e máx de várias notas.

