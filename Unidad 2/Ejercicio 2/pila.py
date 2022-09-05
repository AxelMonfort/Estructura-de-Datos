from nodo import Nodo

class Pila:
    def __init__(self):
        self.__tope = None

    def vacia(self):
        return self.__tope == None

    def insertar(self,dato):
        pila = Nodo()
        pila.setDato(dato)
        pila.setSiguiente(self.__tope)
        self.__tope = pila


    def suprimir(self):
        if self.vacia():
            print('\nPila Vacia.')
        else:
            aux = self.__tope
            self.__tope = aux.getSiguiente()
            return aux.getDato()

    def recorrer(self):
        aux = self.__tope
        if self.__tope == None:
            print('Pila Vacia.')
        else:
            while aux != None:
                print(self.suprimir())
                aux = aux.getSiguiente()