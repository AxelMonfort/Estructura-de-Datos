from Nodo import Nodo

class Cola:
    def __init__(self):
        self.__cantidad = 0
        self.__primerElemento = None
        self.__ultimoElemento = None

    def vacia(self):
        return self.__cantidad == 0

    def insertar(self,dato):
        nuevo = Nodo(dato)
        if self.__ultimoElemento == None:
            self.__primerElemento = nuevo
        else:
            self.__ultimoElemento.setSiguiente(nuevo)
        self.__ultimoElemento = nuevo
        self.__cantidad += 1

    def suprimir(self):
        if not self.vacia():
            aux = self.__primerElemento
            dato = self.__primerElemento.getDato()
            self.__primerElemento = self.__primerElemento.getSiguiente()
            self.__cantidad -= 1
            if self.__primerElemento == None:
                self.__ultimoElemento = None
            del(aux)
            return dato
        else:
            print('\nCola vacia.')

    def recorrer(self):
        aux = Nodo(self.__primerElemento)
        while aux != None:
            print('\n',aux.getDato())
            aux = aux.getSiguiente()
