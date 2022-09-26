"""
    Percentil:
    1- Se refere sempre aos menores valores.
    2- Determina um percentual ordenado desses valores.

    Ex.: lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Pergunta.> Qual é o percentil 50% dessa lista ?

    Resposta.> Bom, nessa lista temos 10 números, logo, 10 itens equivalem
    a 100% da lista. Como foi pedido o percentil 50% dessa lista, 50% dos 10 
    itens equivale a 5 itens. Então agora é só pegar os 5 primeiros itens dessa
    lista e retorná-los!

        Resposta => 1, 2, 3, 4, 5.


    Quartil:
    1- Divide os dados em 4 partes:
         Q1     Q2     Q3              25%    25%    25%    25%
    -----/------/------/------        -----/------/------/------
    min                max             min 1      2      3 max

    Q1 = 25%    Q2 = 50%    Q3 = 75%

    2- Os dados devem estar em ordem crescente.

    Ex.: [13, 25, 69, 72, 33, 41, 28, 17, 65]
    Pergunta.> Qual são os quartís dessa lista ?

    Resposta.> Bom, primeiro tenho que ordenar os números
    em ordem crescente.
        [13, 17, 25, 28, 33, 41, 65, 69, 72]
    Pronto.
    Bom,
        Q1 = 25%    Q2 = 50%    Q3 = 75%
    
    Diferentemente do percentil, o quartil busca somente
    um dado. Logo, o quartil busca o dado que está naquela
    porcentagem da lista (no caso).

            [13, 17, 25, 28, => 50% :33: 50% <= 41, 65, 69, 72]

        Q2 = 50% = 33

            [13, => 25% :17, 25: 25% <= 28, 33, 41, 65, 69, 72]

        Q1 = 25% = (17+25)/2 = 42/2 = 21
        
            [13, 17, 25, 28, 33, 41, => 75% :65, 69: 75% <= 72]

        Q3 = 75% = (65+69)/2 = 134/2 = 67

        Resposta => Q1 = 21  Q2 = 33  Q3 = 67


"""