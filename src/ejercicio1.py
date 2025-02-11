###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

"""
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit
como un número decimal, utilice esta formula para calcular los grados centígrados y retorne
el resultado obtenido. Y viceversa.
"""

def convertir_a_fahrrenheit(centigrados):
    """
    Convierte grados a fahrrenheit de un numero ingresado
    Precodindicion: El Numero ingresado debe ser entero 
    Postcondicion: Retorna el numero de la convercion a fahrenheit
    """
    result= centigrados * 1.8 + 32
    result=round(result,2)
    return result
    #F = ºC x 1.8 + 32
    
def convertir_a_centigrados(fahrenheit):
    """
    Convierte fahrrenheit a grados de un numero ingresado
    Precodindicion: En numero ingresado debe ser flotante
    Postcondicion: Retorna el resultado de la conversion a centigrados
    """
    #ºC = (ºF-32) ÷ 1.8
    result= (fahrenheit-32) / 1.8
    result=round(result,2)
    return result

def asignacion(opcion):# Pide al usuario indicar el valor para convertir a la temperatura a difetentes grados
    """
    Funcion pide que ingrese el valor a convertir al grado deseado
    Precodindicion: Ingresar Numero float
    Postcondicion: Retorntar un numero flotante
    """
    if(opcion==1):
        print('Ingrese Cuantos Grados desea convertir:')
        numero= float(input(''))
    elif(opcion==2):
        print('Ingrese Cuantos Grados desea convertir:')
        numero= float(input(''))
    return numero
    
def menu_opciones(): # Mustra un menu de opciones al ususuario para saber que temperatura convertir
    """
    Esta funcion es un menu que determina a que desea convertir el numero ingresado
    Precodindicion:
    Postcondicion: Se espera un numero entero que puede ser 1 o 2
    """
    print('Este programa convierte grados centigrados a fahrenheit \ntambien de fahrenheit a centrigrados')
    print('Seleccione una opcion para convertir:\n 1 centigrados a fahrenheit\n 2 fahrenheit a centigrados')
    print('-------------------')
    opcion = int(input(''))
    print('-------------------')
    while (opcion != 1 and opcion != 2):
        print('Ingreso un valor invalido ingrese uno correcto:')
        opcion = int(input(''))
        if(opcion==1 or opcion==2):
            opcion= opcion
    if (opcion == 1):
        print('Eligio convertir de centigrados a fahrenheit')
    elif(opcion ==2):
        print('Eligio convertir de fahrenheit a centigrados ')
    return opcion

def principal(): # Invocacion de las funciones creadas
    opcion=menu_opciones()
    numero= asignacion(opcion)
    result_fah= convertir_a_fahrrenheit(numero)
    result_centi= convertir_a_centigrados(numero)
    if opcion==2:
        print('El resultado es ...')
        print(f'fahrenheit: {numero}')
        print(f'Centigrados:{result_centi:10.2f}')
    else:
        print('El resultado es...')
        print(f'Centigrados: {numero}')
        print(f'Fahrenheit: {result_fah}')
if __name__ == '__main__':
    principal()