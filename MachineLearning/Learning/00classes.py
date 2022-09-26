#Classes e métodos
class DidaticaTech:
    def incrementa(self, v, i):     #Atributos: v, i
        valor = v
        incremento = i
        resultado = valor + incremento
        return resultado

a = DidaticaTech()
b = a.incrementa(10,1)

a = DidaticaTech().incrementa(10,1)

#print(a)

# ----------
#Ex.: self 
# ----------
class DidaticaTech2:
    def incrementa(self, v, i):     #Atributos: v, i
        self.valor = v
        self.incremento = i
        self.resultado = self.valor + self.incremento
        return self.resultado
a = DidaticaTech2()
b = a.incrementa(12, 1)

# print(a.valor)

# ------------------------
#Método Construtor __init__
# ------------------------
class DidaticaTech3:
    def __init__(self, v: int, i: int):     #Atributos: v, i
        self.valor = v
        self.incremento = i
    def incrementa(self):
        self.valor += self.incremento

a = DidaticaTech3(15,5)
a.incrementa()

# print(a.valor)

b = DidaticaTech3(20,3)
b.incrementa()

# print(b.valor)

# ------------------------------------------------------
#Método Construtor __init__ definindo valores padrões
# ------------------------------------------------------
class DidaticaTech4:
    def __init__(self, v=10, i=8):     #Atributos: v, i
        self.valor = v
        self.incremento = i
    def incrementa(self):
        self.valor += self.incremento

a = DidaticaTech4()
a.incrementa()

# print(a.valor)

# Depois de instanciarmos -> a = DidaticaTech4(). quando executamos
# a.incrementa(), o que o interpretador está fazendo é:
# DidaticaTech4().incrementa(a, 10, 8)

#-----------------------------------------------------------------------

class DidaticaTech5():
    def __init__(self, v=17, i=2):     #Atributos: v, i
        self.valor = v
        self.incremento = i
        self.valor_exponencial = v
    def incrementa(self):
        self.valor += self.incremento
    def verifica(self):
        if self.valor > 12:
            print("Ultrapassou 12")
        else:
            print("Não ultrapassou 12")
    def exponencial(self, e):
        self.valor_exponencial = self.valor**e
    def incrementa_quadrado(self):
        self.incrementa()
        self.exponencial(2)

# variável a
a = DidaticaTech5()
a.incrementa()
# print(a.valor)

# a.verifica()

a.exponencial(3)
# print(a.valor_exponencial)

a.incrementa_quadrado()
# print(a.valor_exponencial)

# variável b
b  = DidaticaTech5(50, 5)
b.incrementa()
# print(b.valor)

# ----------
# Herança
# ----------
class Calculos(DidaticaTech5):
    pass

c = Calculos()
c.incrementa_quadrado()
# print(c.valor_exponencial)

# ----------------------------------

class Calculos2(DidaticaTech5):
    def decrementa(self):
        self.valor -= self.incremento

c = Calculos2()
c.decrementa()
# print(c.valor)

# ----------------------------------

class Calculos3(DidaticaTech5):
    def __init__(self, d=5):
        super().__init__(v=17, i=2) #Herda atributos da super classe (DidaticaTech5).
        self.divisor = d
    def decrementa(self):
        self.valor -= self.incremento
    def divide(self):
        self.valor /= self.divisor

c = Calculos3()
c.incrementa()
# print(c.valor)
c.divide()
print(c.valor)