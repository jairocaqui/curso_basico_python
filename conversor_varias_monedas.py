def conversor(tipo_pesos, valor_dolar):
    pesos=float (input("Cuantos peso"+tipo_pesos+" tienes? "))
    cambio=str(round(   pesos/valor_dolar ,2))
    print("tienes $" +  cambio+" dolares")



menu="""
Bienvenido al conversor de monedas 
1.- Pesos colombianos
2.- Pesos Argentinos
3 .- Pesos mexicanos

Eliga una opcion :"""

opcion=int(input(menu))
if opcion==1:
    conversor("colombianos", 3875)
elif opcion==2:
    conversor("argentinos", 65)
elif opcion== 3:
    conversor("mexicanos", 24)
else:
    print("Ingreso una opcion incorrecta")