###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

"""
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.
"""
def division_lenta(dividendo, divisor):
    resto=0
    cociente=0
    div= dividendo - divisor
    while div>=0: # Se repite las veces necesarias para encontrar el cociente y el resto de la division
        cociente +=1
        div-= divisor
    resto= div + divisor
    return cociente

def resto(dividendo, divisor):
    div= dividendo - divisor
    while div>=0:
        div-= divisor
    resto= div + divisor
    return resto

def principal():
    print("Ingrese 2 numero para realizar la divicion")
    num1=float(input("Valor 1: "))
    num2= float(input("Valor 2: "))
    while num2<=0:
        print("El valor de numero 2 debe ser distinto de 0")
        num2= float(input("Ingrese valor correcto: "))
    cociente= division_lenta(num1,num2)
    reesto= resto(num1,num2)
    print(f"Cociente: {cociente} Resto: {reesto}")
    
if __name__ == "__main__":
    principal()