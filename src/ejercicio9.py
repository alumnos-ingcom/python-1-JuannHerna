###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

"""
Escribir una función que retorne una tuple con factores primos de un numero entero positivo
"""
def factores_primos(numero):
    """
    factores primos es una funcion en la cual ingresa un numero y determina sus factores primos
    Precodindicion: Numero debe ser entero mayor a 0
    Postcondicion: Retorna tupla con los factores primos del numero ingresado
    """
    factor_primo=2
    resto=0
    factor=[]
    while numero > 1:
        if numero% factor_primo==0:
            agregar=factor_primo
            factor.append(agregar)
            numero= numero// factor_primo
        else:
            factor_primo+=1
    factores = tuple(factor)
    return factores
    
def principal():
    print("Ingrese un numero para determinar los factores primos:")
    num=int(input(""))
    result =factores_primos(num)
    print(f"Los Factores de {num} son: {result}")
if __name__ == '__main__':
    principal()

