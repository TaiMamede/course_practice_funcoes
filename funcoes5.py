'''
Parametros *args e **Kwargs
def <identificador> (*args **kwargs)
*args retorna tuple
**kwargs retorna dict
utilizamos quando nao sabemos a quantidade de parâmetros
'''
def soma(*args):
  print(args)

soma(1,2,3,4,5)

##########################################################
def soma(*args):
    total = 0
    for i in args:
        total += i
    return total

print(soma(1,2,3,4,5,6,7))

########################################################

def soma(*args):
    return sum(args)

print(soma(1,2,3,4,5,6,7))

#######################################################



