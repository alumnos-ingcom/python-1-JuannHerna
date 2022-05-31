###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

"""
Escribir un programa que permita transformar un número solicitado expresado en grados, minutos y segundos a segundos a segundos.
Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.

Recuerden que un grado son 60 minutos y un minuto son 60 segundos.
"""
def sexadecimal_a_decimal(horas, minutos, segundos):
    seg_totales=0
    if horas>0: #convierte hs a seg
        seg_totales+= horas * 3600
    if minutos>0: ##Convierte min a seg
        seg_totales+= minutos*60
    if segundos>0:
        seg_totales+= segundos
    return seg_totales

def decimal_a_sexadecimal(numero):
    while 
    

def principal():
    print("Este programa convierte segundos a horas minutos y segundos")
    print("Tambien de horas, minutos y segundos a segundos")
    print("Elija la opcion que desee:")
    print("1. Horas, min y seg a seg \n2. Segundos a hs, min y seg") 
    opcion=int(input(""))
    if opcion==1:
        print("Ingrese valores: ")
        hs= int(input("Horas:"))
        minutos= int(input("Minutos:"))
        seg= int(input("Segundos:"))
        result_seg= sexadecimal_a_decimal(hs, minutos, seg)
        print(f"las horas minutos y segundos transdormados a segundos son: {result_seg} seg")
    elif opcion==2:
        print("Ingrese un valor a transformar")
        num=int(input(""))
        resultado_sexa= decimal_a_sexdecimal(num)
        print(f"Los segundos transdormados a horas minutos y segundos: {resultado_sexa} ")
if __name__ == "__main__":
    principal()