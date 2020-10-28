print ("Bienvenido a tu conversor de monedas")
print("Para cambiar DOLARES escriba 1 ")
print("Para cambiar SOLES  escriba  2")
sel_tipo_ope= input("Ingrese la opcion :")

if sel_tipo_ope == "1":
    cantidad_cambiar=int(input("Ingrese cuantos dolares desea cambiar:  "))
    cambio=str(cantidad_cambiar*3.63)
    print("El cambio de tus Dolares a Soles es " + cambio)

if sel_tipo_ope == "2":
    cantidad_cambiar=int(input("Ingrese cuantos soles desea cambiar:  "))
    cambio=str(cantidad_cambiar/3.63)
    print("El cambio de tus Soles a Dolares es " +cambio)