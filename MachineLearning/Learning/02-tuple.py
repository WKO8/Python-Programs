
lista = [2, 4, 7]
lista[0] = 20
print(lista)
del lista[0]
print(lista)


tupla = (6, 8, 4)
#tupla[0] = 30
#del tupla[1]
print(tupla[0])

novaTupla = tuple(lista)
print(novaTupla)

numero = (3)
print(type(numero)) # Retorna int, pq pra ser uma tupla deve ter uma vírgula

numero1 = (1,)
print(type(numero1)) # Retorna tuple, pq tem uma vírgula entre ().