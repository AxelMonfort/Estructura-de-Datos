class Nodo:
    __dato = None
    __siguiente = Nodo = None

    def __init__(self,dato, siguiente:Nodo = None):
        self.__dato = dato
        self.__siguiente = siguiente

    def setSiguiente(self,siguiente:Nodo=None):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def setDato(self,dato):
        self.__dato = dato

    def getDato(self):
        return self.__dato