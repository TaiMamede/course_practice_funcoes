"""
Funções com Parâmetro
"""

def area_circulo(raio):
    PI = 3.141592
    area = PI * pow(raio, 2)
    return area

def area_cilindro(raio, altura):
    area = area_circulo(raio) * altura
    return area

r = float(input("Digite o valor do raio do cilindro: "))
h = float(input("Digite a altura do cilindro: "))
a = area_cilindro(r, h)
print(f"O valor da area do cilindro é {a}")

