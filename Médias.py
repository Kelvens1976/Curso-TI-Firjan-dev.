def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    if b!=0:
     return a/b
    else:
       print("Não é possível fazer essa operação")
a = float(input("informe o valor de a: "))
b = float(input("informe o valor de b: "))
resultado = soma(a,b)
print("o resultado da soma é:", resultado) 
resultado1 = subtracao(a,b)
print("o resultado da subtração é:", resultado1) 
resultado2 = multiplicacao(a,b)
print("o resultado da multiplicação é:", resultado2)
resultado3 = divisao(a,b)
print("o resultado da divisão é:", resultado3)