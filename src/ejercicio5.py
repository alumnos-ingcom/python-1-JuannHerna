###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

"""
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.
"""
def division_lenta(dividendo, divisor):
    """
    Division lenta retorna el cociente de la division
    Precodindicion: Los numeros deben ser flotantes
    Postcondicion: Resultado deber ser un tupla con resto y cociente de la division
    """
    signo= 0
    cociente=0
    resto=0
    if divisor<0:
        divisor= divisor* -1
        signo= -1
    if dividendo<0:
        dividendo= dividendo* -1
        signo= -1
    div= dividendo - divisor
    while div>=0: # Se repite las veces necesarias para encontrar el cociente y el resto de la division
        cociente +=1
        div-= divisor
    if signo==-1:
        cociente*= signo
    resto= div + divisor
    result= cociente, resto
    return result


def principal():
    print("Ingrese 2 numero para realizar la divicion")
    num1=float(input("Valor 1: "))
    num2= float(input("Valor 2: "))
    while num2==0:
        print("El valor de numero 2 debe ser distinto de 0")
        num2= float(input("Ingrese valor correcto: "))
    cocient_rest= division_lenta(num1,num2)
    print("El cociente y el resto de la divicion son los sig: ", cocient_rest)
    
if __name__ == "__main__":
    principal()