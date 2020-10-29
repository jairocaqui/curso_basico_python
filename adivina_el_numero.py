import random


def run():
    num_aleatorio=random.randint(1,100)
    num_user= int(input("Que numero penso la CPU "))
    while  num_user != num_aleatorio:
        if num_user < num_aleatorio:
            print("Subele no seas malo")
        else:
            print("Bajale un poquito")
        num_user= int(input("Que numero penso la CPU "))
    print("Ganaste")


if __name__ == "__main__":
    bienvenida="""
    Intenta ganarle a la Maquina 
    piensa un numero del 1 al 100 
    """
    print (bienvenida)
    run()