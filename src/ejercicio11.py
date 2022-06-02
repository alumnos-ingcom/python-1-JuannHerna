###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############
"""
Escribir una función que indique con True si un número entero es multiplo de otro, utilizando sumas y restas.
"""
def es_multiplo(numero, multiplo):
    """
    Esta funcion determina si un numero es multiplo de otro
    """
    aux=numero
    cont=0
    result= False
    while aux>0:
        result= aux-multiplo
        aux= result
    if result==0:
        result= True
        
    return result
    
def principal():
    print("Ingrese dos numero para determinar si es multiplo:")
    num=int(input("Numero a averiguar: "))
    multiplo=int(input("Multiplo: "))
    result =es_multiplo(num,multiplo)
    if result== True:
        print(f"{num} es multiplo de {multiplo}")
    else:
        print(f"{num} no es multiplo de {multiplo}")
if __name__ == '__main__':
    principal()