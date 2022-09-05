from pila import Pila

if __name__ == '__main__':
    pila = Pila()
    numero = int(input('\nIngrese numero: '))
    resultado,anterior = 0,numero-1
    resultado += numero * anterior
    while anterior > 1:
        anterior -= 1
        if anterior != 1:
            resultado = resultado * anterior

    pila.insertar(resultado)
    pila.recorrer()