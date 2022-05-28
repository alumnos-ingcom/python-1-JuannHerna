###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############
"""
Escribir una función que indique con True si un numero indicado es Primo.
"""
def es_primo(numero):
    cont=0
    result=0
    for n in range(1,numero+1):
        if numero% n == 0:
            cont+=1
    if cont>2:
        result= False
    elif cont==2:
        result= True        
    return result

def principal():
   print("Ingrese un numero para determinar si es primo: ")
   num= int(input())
   resulta=es_primo(num)
   print(f"El numero ingresado es primo? {resulta}") 

if __name__ == "__main__":
    principal()