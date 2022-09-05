import numpy as np

class PilaSecuencial:
    __arreglo = None
    __tope = None
    __cant = None

    def __init__(self,cant=2):
        self.__tope = 0
        self.__cant = cant
        self.__arreglo = np.empty(self.__cant,dtype=int)

    def getTamanio(self):
        return len(self.__arreglo)

    def vacia(self):
        return self.__tope == 0

    def insertar(self,objeto):
        if self.__tope <= self.__cant:
            self.__arreglo[self.__tope] = objeto
            self.__tope += 1
        else:
            print('\nTope Maximo.')

    def suprimir(self):
        if self.vacia():
          print('\nPila Vacia.')
        else:
            self.__tope -=1
            self.__arreglo[self.__tope]
            np.delete(self.__arreglo,self.__tope)
            self.__tope -= 1
            print('\n Se elimino el objeto ')

    def mostrar(self):
        if not self.vacia():
            for i in range(self.__tope):
                print (self.__arreglo[i])

if __name__ == '__main__':
    pila = PilaSecuencial()
    pila.insertar(2)
    pila.insertar(4)
    pila.mostrar()
    pila.suprimir()
    pila.mostrar()