"""
Funções com Parâmetro Patrao
Função chamada potencia: com um parâmetro calcula o quadrado do numero, dois parâmetros o segundo
será utilizado como o valor da potencial.
"""

def potencia(numero, expoente=2):
    resultado = pow(numero, expoente)
    return resultado

n = float(input("Digite o número: "))
e = int(input("Expoente: "))

print(f"Valor com expoente: {potencia(expoente=e, numero=n)}")
print(f"Valor sem expoente: {potencia(n)}")

