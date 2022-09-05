from pila import Pila as pila

if __name__ == '__main__':
    band = False
    binario = pila()
    numero = int(input('\nIngrese numero: '))
    while band == False:
        division = int(numero / 2)
        x = numero%2
        binario.insertar(x)
        numero = division
        if division == 1 or division == 0:
            binario.insertar(numero%2)
            band = True

    print(binario.recorrer())