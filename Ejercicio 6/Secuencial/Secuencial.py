class Cola:
    def __init__(self,max):
        self.__lista = []
        self.__maximo = max
        self.__primerElemento = 0
        self.__ultimoElemento = 0
        self.__cantidad = 0

    def vacia(self):
        return self.__cantidad == 0

    def llena(self):
        return self.__cantidad == self.__maximo

    def insertar(self,dato):
        if not self.llena():
            self.__lista.insert(self.__ultimoElemento,dato) #self.__lista.append(dato)
            self.__ultimoElemento = (self.__ultimoElemento + 1) % self.__maximo   #Cuando de cero es pq el ultimo es igual al maximo.
            self.__cantidad += 1
        else:
            print('\nCola llena.')

    def suprimir(self):
        if not self.vacia():
            x = self.__lista[self.__primerElemento]
            self.__primerElemento = (self.__primerElemento + 1) % self.__maximo #Esto da cero cuando la cola este vacía.
            self.__cantidad -= 1
            return x
        else:
            print('\nCola Vacia.')

    def recorrer(self):
        for i in range(self.__cantidad,0,-1):
            print(self.__lista[i])