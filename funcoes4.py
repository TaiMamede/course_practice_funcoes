def potencia(numero, expoente=2):
    """Função que calcula a potencia de um número valor de Entrada:
    numero - numero a ser calculado (elevado a potencia(float))
    expoente - expoente a ser utlizado no calculo(inteiro)

    Resultado:
    Resultado ao calculo da potencia(float)"""
    resultado = pow(numero, expoente)
    return resultado

n = float(input("Digite o número: "))
e = int(input("Expoente: "))


print(f"Valor com expoente: {potencia(expoente=e, numero=n)}")
print(f"Valor sem expoente: {potencia(n)}")
help(potencia)
