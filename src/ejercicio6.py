###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

"""
Escribir una función que a partir de tres variables de tipo entero retorne una tupla con dichos valores ordenados de menor a mayor.
Y Viceversa
"""
def ordenar_mayor_a_menor(uno, dos, tres):
    lista=[uno, dos, tres]
    for j in range(1,len(lista)):
        for i in range(len(lista)-1):
             if lista[i]<= lista[i+1]:
                 aux= lista[i]
                 lista[i]=lista[i+1]
                 lista[i+1]=aux
    return lista
    
def ordenar_menor_a_mayor(uno, dos, tres):
    lista=[uno, dos, tres]
    cont=0
    i=0
    for j in range(1,len(lista)):
        for i in range(len(lista)-1):
            if lista[i]>= lista[i+1]:
                aux= lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux

    return lista
    
def principal():
    print("Ingrese 3 numero para ordenarlo de mayor a menor")
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 2: "))
    num3=int(input("Numero 3: "))
    opcion= int(input("Ingrese como desea ordenar \n.1 Mayor a Menor \n.2 Menor a Mayor\n"))
    if opcion ==1:
        lista=ordenar_mayor_a_menor(num1,num2,num3)
    elif opcion==2:
        lista=ordenar_menor_a_mayor(num1,num2,num3)
    print(f"La lista ordenada queda de la siguiente forma: {lista}")
    
if __name__ == "__main__":
    principal()