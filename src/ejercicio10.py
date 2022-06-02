###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

"""
Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo.
Palíndromo,es si se lee igual de derecha a izquierda que de izquierda a derecha.
"""
def es_palindromo(texto):
    """
    Esta funcion determina si un numero o una frase son palindromas
    """
    text1=texto
    maxx=len(text1)
    tex_reves=''
    cont=0
    result= False
    for i in range(maxx):
        tex_reves+= text1[-i-1]    
    
    for j in range (maxx):
        if tex_reves[j]== text1[j]:
            cont+=1
    if cont==maxx:
        result= True
    return result

def principal():
    print("Este programa determina si la palabra o frase es palindromo \nPalindromo es si se lee igual de derecha a izquierda que de izquierda a derecha")
    print("Ingrese palabra a determinar: ")
    palabra= input("")
    palabra =palabra.lower()
    res_palabra=es_palindromo(palabra)
    print(f"Es palindroma: {res_palabra}")
if __name__ == '__main__':
    principal()