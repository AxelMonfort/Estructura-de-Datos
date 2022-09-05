class Nodo:
    def __init__(self,dato):
        self.__dato = dato
        self.__siguiente = None

    def getDato(self):
        return self.__dato

    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
