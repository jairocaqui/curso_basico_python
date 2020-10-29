
def run ():
    num=int(input("Ingrese hasta que numero se mostraran las potencias: "))
    cont=0
    while cont<=num:
        print (2**cont)
        cont=cont+1


if __name__ == "__main__":
    run()