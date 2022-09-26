import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

arquivo = pd.read_csv("C:/Users/T-Gamer/Desktop/Meus Dados/Meus Dados/Programação/Programas Python/Machine Learning/Scripts/Classificando Vinhos/datasets_16721_22034_wine_dataset.csv")

arquivo['style'] = arquivo['style'].replace('red', 0)       # Mudando na coluna 'style' 'red' por 0
arquivo['style'] = arquivo['style'].replace('white', 1)     # Mudando na coluna 'style' 'white' por 1

# Separando as variáveis entre preditoras e alvo (a que vamos prever).
y = arquivo['style']
x = arquivo.drop('style', axis = 1)


# Criando os conjuntos de dados de treino e teste:
#   train_test_split(preditoras, alvo, porcentagem_para_teste_e_treino)  
#       Ex.> train_test_split(x, y, test_size = 0.3)  30% de todos os dados para teste e 70% para treino.
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)
# OBS.: É necessário que as variáveis estejam nessa ordem, todos os "x" e "treino" primeiro e depois todos os "y" e "teste"
# Devido ao uso da função train_test_split() que pelo próprio nome já diz, dividido entre treino e teste.


#Criação do modelo:
modelo = ExtraTreesClassifier(n_estimators=100)
modelo.fit(x_treino, y_treino)  # Realiza o treino, estudo dos padrões dos dados (x_treino e y_treino)

#Imprimindo resultados:
resultado = modelo.score(x_teste, y_teste)  # Classifica os dados (x_teste) e compara com o gabarito (y_teste) se ele acertou ou errou.
print("Acurácia:", resultado)

print(y_teste[400:403])
print(x_teste[400:403])

previsoes = modelo.predict(x_teste[400:403])
print(previsoes)
