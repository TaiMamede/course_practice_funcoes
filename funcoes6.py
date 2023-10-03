'''
def <identificador> (**kwargs)
**kwargs retorna dict

Importante: Parametros... ORDEM
>>Parametros Definidos
>>*args
>>Parametros Nomeados
>>**Kwargs
'''

def favorite_food(**kwargs):
    print(kwargs)

favorite_food(ana='cabalhoada', marcelo='risoto', adriana='camarao')

#####################################################################

def favorite_food(**kwargs):
    for chave in kwargs:
        print(f"{chave} gosta de {kwargs[chave]}")


favorite_food(ana='cabalhoada', marcelo='risoto', adriana='camarao')

#####################################################################