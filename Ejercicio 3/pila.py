from Nodo import Nodo

class Pila:
    def __init__(self):
        self.__tope = None

    def insertar(self,dato):
        pila = Nodo()
        pila.setDato(dato)
        pila.setSiguiente(self.__tope)
        self.__tope = pila

    def vacia(self):
        return self.__tope == None

    def suprimir(self):
        if self.vacia():
            print('\nPila vacia.')
        else:
            aux = self.__tope
            self.__tope = aux.getSiguiente()
            return aux.getDato()

    def recorrer(self):
        aux = self.__tope
        if aux == None:
            print('\nPila Vacia.')
        else:
            while aux != None:
                print(self.suprimir())
                aux = aux.getSiguiente()