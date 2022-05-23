###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

"""
Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero utilizando sumas y restas.

"""
def signo(numero):
    num= numero
    minimo=0
    if numero> minimo:
        print(f"El numero {numero} es positivo")
    elif numero<minimo:
        print(f"El numero {numero} es negativo")
    elif numero== minimo:
        print("Numero es 0")

def principal():
    numero=int(input("Ingrese numero: "))
    signo(numero)

if __name__ == "__main__":
    principal()