###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

"""
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""

def compara(numero, otro_numero):
    """
    Compara 2 numeros para determinar cual es mayor o si son iguales
    """
    num1= numero
    num2= otro_numero
    
    result= num1-num2
    
    if result<0:
        retorno= -1
    elif result== 0:
        retorno= 0
    elif result>0:
        retorno= 1
    return retorno
    
def principal():
    print("Ingrese 2 valores para determinar cual es mayor")
    num1=int(input("Primer valor: "))
    num2=int(input("Segundo valor: ")) #Guarda los valores ingresados para pasarselo a la funcion compara
    
    resultado=compara(num1, num2) # Invoca la funcion y guarda el resultado en la variable reultado
    
    if resultado<0:
        print("El segundo numero es mayor al primero")
    elif resultado>0:
        print("El primer numero es mayor al segundo")
    elif resultado==0:
        print("Los numero son iguales")
        
if __name__ == "__main__":
    principal()