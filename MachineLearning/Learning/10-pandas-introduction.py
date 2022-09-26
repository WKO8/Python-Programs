import pandas as pd
import numpy as np

alunos = {'Nomes':['Ricardo', 'Pedro', 'Roberto', 'Carlos'],
         'Nota':[4, 7, 5.5, 9],
         'Aprovado':['Não','Sim','Não','Sim']}

dataframe = pd.DataFrame(alunos)

# print(dataframe)

objeto1 = pd.Series([2, 6, 9, 10, 5])

# print(objeto1)

array1 = np.array([6, 12, 2, 9, 10])
array2 = np.array([(2, 6, 9, 10, 5),  (6, 12, 2, 9, 10)])

# print(array1)
# print(array2)

objeto2 = pd.Series(array1)

print(objeto2)