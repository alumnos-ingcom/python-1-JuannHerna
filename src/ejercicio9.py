###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

"""
Escribir una función que retorne una tuple con factores primos de un numero entero positivo
"""
def factores_primos(numero):
    factor_primo=2
    resto=0
    factores=[]
    while numero > 1:
        if numero% factor_primo==0:
            agregar=factor_primo
            factores.append(agregar)
            numero= numero// factor_primo
        else:
            factor_primo+=1   
    return factores
    
def principal():
    print("Ingrese un numero para determinar los factores primos:")
    num=int(input(""))
    result =factores_primos(num)
    print(f"Los Factores de {num} son: {result}")
if __name__ == '__main__':
    principal()

