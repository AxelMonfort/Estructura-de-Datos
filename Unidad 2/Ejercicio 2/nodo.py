class Nodo:
    def __init__(self):
        self.__dato = None
        self.__siguiente = None

    def getDato(self):
        return self.__dato

    def setDato(self,dato):
        self.__dato = dato

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente