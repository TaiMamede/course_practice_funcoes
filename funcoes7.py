'''
Challenge: Faça uma função em Python que retorne o valor lógico True se o número inteiro
 passado por parâmetro for primo, e False se não.
 Implemente sua função em um programa completo.
 Obs.: um número é primo se for divisível por 1 e por ele mesmo.
'''

def primo(numero):
    """ Função logica que retorna True se o valor informado for primo
    Entrada: numero = numero inteiro
    Retorna: True se o numero for primo e False se o numero não for primo"""

    eprimo = False
    resto_zero = 0

    for i in range(1, numero):
        if (numero%i)==0:
            resto_zero += 1

    if resto_zero == 1:
        eprimo = True

    return eprimo

n = int(input("Entre com um valor inteiro, positivo e maior que 0: "))

if primo(n):
    print(f"O numero {n} é primo.")
else:
    print(f"O numero {n} NÃO é primo.")


