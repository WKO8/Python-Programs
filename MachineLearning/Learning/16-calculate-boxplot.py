""" BoxPlot -> Diagrama/Gráfico de caixa

        º
        º
       _º_ LS
        │
      __│__ -> Q3
AIQ <-│___│-> Mediana
    `-│___│-> Q1
        │
       _│_ LI
        º

AIQ = Amplitude InterQuartil
LS = Limite Superior = Q3 + 1.5*(Q3-Q1)       Terceiro quartil somado à amplitude interquartil multiplicado a uma constante (1.5 no caso)
LI = Limite Inferior = Q1 - 1.5*(Q3-Q1)       Primeiro quartil subtraído à amplitude interquartil multiplicado a uma constante (1.5 no caso)

    (-2, 3, 5, 8, 9, 11, 13, 14, 15, 17, 35)

Mediana = 11
Q1 = 5
Q3 = 15                         30   _º_
LS = 15+1.5(15-5)               25    │
     15+1.5*10                  20    │
     15+15                      15   _│_
     30                         10  │---│
                                5   │___│
LI = 5-1.5*10                   0     │
     5-15                      -5     │
     -10                       -10   _│_

"""


