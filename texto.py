# nombre="jairo"
# print (nombre[:])
# print (nombre[::-1])

def palindromo(palabra):
    palabra=palabra.replace(' ','').lower()
    #palabra_invertida=palabra[::-1]
    #if palabra==palabra_invertida:
    if palabra==palabra[::-1]:
        return True
    else:
        return False


def run():
    palabra=input("Escriba una palabra ")
    es_polidromo=palindromo(palabra)
    if es_polidromo==True:
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == "__main__":
    run()