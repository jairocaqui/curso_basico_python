import random

def generar_contrasena():
    mayuscula=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    minuscula=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','W','x','y','z']
    simobolos=['!','#', '$', '&', '/', '(', ')']
    numeros=[1,2,3,4,5,6,7,8,9,0]

    #la contraseña tendra 15 caracteres 
    caracteres=mayuscula+minuscula+simobolos+numeros #une todas listas se unen 
    contrasena=[]                                     #se crea una lista vacia  
    for i in range(15):
        caracter_random = random.choice(caracteres) #la opcion choice elige un caracter de la lista
        contrasena.append(caracter_random)          #luego agrega a la lista el caracter elegido
       
    # contrasena = "".join(contrasena)                
    # return contrasena
    
    contrasena  = "".join(map(str,contrasena))       #convierte la lista en string  string.join conecta elementos dentro de la lista de cadenas, no ints.
    return contrasena
    


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es : '+ contrasena)


if __name__ == "__main__":
    run()