def somaQuadrados(a, b):
    somaQ = a**2 + b**2
    return somaQ

print(somaQuadrados(2,3))

somaQuadrados2 = lambda a, b: a**2 + b**2 #name = lambda parameters: code

print(somaQuadrados2(2,3))

x = lambda f: f/2

print(x(8))