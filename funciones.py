def conversacion(mensaje):
    print("Hola") 
    print("como estas") 
    print("Elegiste la opcion "+mensaje)
    print("Adios")


opcion=int(input("Elige una opcion 1,2,3: "))
if      opcion== 1:
    conversacion(str(opcion))
elif    opcion== 2:
    conversacion(str(opcion))
elif    opcion== 3:
    conversacion(str(opcion))
else:
    print("Ingresa la opcion correcta")