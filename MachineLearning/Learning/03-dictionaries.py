#dicionario = {chave:valor}
dicionario = {'Curso':'Python para ML',
              'Produtor':'Didática Tech',
              'Preço':'Gratuito',
              'Nota':10}

a = dicionario['Preço']
print(a)

dicionario['Preço'] = 'R$300,00'
print(dicionario)

dicionario['Pré-requisito'] = 'Python Básico'
print(dicionario)

print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())
print(dicionario.clear())