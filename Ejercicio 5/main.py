from pila import Pila

def inicio(discos):
    for i in range(discos,0,-1):
        pila1.insertar(i)

def fin():
    return pila1.vacia() and pila2.vacia() and pila3.llena()

def estadoInicial():
    print('\nESTADO: ')
    for i in range(len(listaP)):
        print('\nPila ',i+1)
        listaP[i].recorrer()

def verificar():
    origen = int(input('\nIngrese pila de origen: '))
    while origen == [1,2,3]:
        origen = int(input('\nError, vuelva a ingresar: '))

    destino = int(input('\nIngres pila de destino: '))
    while destino == [1,2,3]:
        destino = int(input('\nError, vuelva a ingresar: '))

    return origen,destino


def juego():
    disco = verificar()
    origen = listaP[disco[0]-1]
    destino = listaP[disco[1]-1]
    if not origen.vacia() and not destino.llena():
        if destino.vacia() or origen.getDato() < destino.getDato():
            destino.insertar(origen.suprimir())
            global cant
            cant += 1
        else:
            print('\nMovimiento invalido.')
    else:
        print('\n Pila vacia.')
    estadoInicial()


if __name__ == '__main__':
    print('-----------TORRES DE HANOI------------')
    print('\n¡¡¡Que comience el juego!!!')
    discos = int(input('\nIngrese la cantidad de discos: '))
    pila1 = Pila(discos)
    pila2 = Pila(discos)
    pila3 = Pila(discos)
    listaP = [pila1,pila2,pila3]  #lista de pilas
    cant = 0    #movimientos en el juego

    inicio(discos)
    estadoInicial()

    while not fin():
        juego()

    print('\n¡¡¡Felicitaciones, completo el juego!!!.')
    print('\nLa cantidad de movimientos fue de: ',cant)
    print('\n\n\n Numero minimo de movimientos: ',2*discos-1)