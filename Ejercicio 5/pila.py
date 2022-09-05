class Pila:
    def __init__(self,xcant):
        self.__lista = []
        self.__tope = -1
        self.__cant = xcant


    def vacia(self):
        return self.__tope == -1

    def llena(self):
        return self.__tope == self.__cant-1

    def insertar(self,numero):
        if not self.llena():
            self.__tope += 1
            self.__lista.insert(self.__tope, numero)
        else: print('\nPila llena.')

    def suprimir(self):
        if not self.vacia():
            x = self.__lista[self.__tope]
            self.__tope -= 1
            return x
        else: print('\nPila vacia.')

    def recorrer(self):
        if not self.vacia():
            for i in range(self.__tope,-1,-1):
                print('\t\t',self.__lista[i])
        else:
            print('\nPila vacia.')

    def getDato(self):
        return self.__lista[self.__tope]