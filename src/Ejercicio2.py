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
        signo=1
    elif numero<minimo:
        print(f"El numero {numero} es negativo")
        signo= -1
    elif numero== minimo:
        print("Numero es 0")
        signo=0
    return signo

def principal():
    print("Este programa determina si un valor es positvo o negativo")
    numero=int(input("Ingrese numero: "))
    sgn=signo(numero)
    if sgn== -1:
        print(f"El numero es negativo")
    elif sgn==1:    
        print(f"El numero  es positivo")
    else:
        print("Numero es 0")
if __name__ == "__main__":
    principal()