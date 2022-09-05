from nodo import Nodo

class encadenada:
    __cant = 0
    __tope = Nodo=None

    def __init__(self):
        self.__tope = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0

    def insertar(self,dato):
        self.__tope = Nodo(dato,self.__tope)
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            print('\nPila vacia.')
            return 0
        else:
            aux = self.__tope
            self.__tope.getSiguiente()
            self.__cant -= 1
            del(aux)

    def recorrer(self):
        aux = self.__tope
        if aux == None:print('\nNo hay elementos en la lista')
        else:
            self.__tope = aux.getSiguiente()
            print(aux.getDato())


pila = encadenada()
#pila.insertar(5)
#pila.insertar(4)
#pila.insertar(3)
#pila.suprimir()
#pila.recorrer()
#pila.recorrer()
#pila.recorrer()