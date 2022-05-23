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
    print(f"Cociente: {cociente} Resto: {div+divisor}") # div+divisor lo que hace es que como el valor de la resta queda negativo para cortar el while
                                                        #para cortar el bucle se le suma el divisor para que de el resto

def principal():
    print("Ingrese 2 numero para realizar la divicion")
    num1=int(input("Valor 1: "))
    num2= int(input("Valor 2: "))
    while num2<=0:
        print("El valor de numero 2 debe ser distinto de 0")
        num2= int(input("Ingrese valor correcto: "))
    division_lenta(num1,num2)

if __name__ == "__main__":
    principal()