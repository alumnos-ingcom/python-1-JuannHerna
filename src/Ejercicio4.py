###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

"""
Escribir una función que haga la suma entre dos números enteros sin hacer la operación de manera directa.
Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""
def suma_lenta(numero, otro_numero):
    num2= otro_numero
    num1= numero
    resultado=num1
    while num2<0 or num2>0: #Se repite dependiendo si es positivo o negativo para hacer la suma lenta
        if num2>0:
            resultado += 1    
            num2-=1
        elif num2<0:
            resultado -= 1
            num2+=1
    print(f"La suma entre {num1} y {otro_numero} es : {resultado}")     
    
    
def principal():
    print("Ingrese 2 valores para sumar")
    nume1=int(input("Numero 1:"))
    nume2=int(input("Numero 2:"))
    suma_lenta(nume1, nume2)
    
if __name__ == "__main__":
    principal()