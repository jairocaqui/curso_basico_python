def run():
    poblacion_paises={
        'Argentina':44938712,
        'Brasil':210147125,
        'Colombia':50372424
    }
    
    #print(poblacion_paises)# muestra sus claves y valores
    #print(poblacion_paises['Argentina']) # muestra solo el valor de clave "Argentina"
    #print(poblacion_paises[44938712]) # Sale error no se puede imprimir individualmentela clave

    #Recorriendo el diccionario

    # for pais in poblacion_paises: ##si no se coloca ningun metodo solo muestra las claves
    #    print(pais)

    # for pais in poblacion_paises.keys(): ##muesra las claves del diccionario 
    #     print(pais)

    # for pais in poblacion_paises.values(): ## muestra los valores del diccionario
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print (pais +" tiene "+ str(poblacion)+" habitantes")

if __name__ == "__main__":
    run()