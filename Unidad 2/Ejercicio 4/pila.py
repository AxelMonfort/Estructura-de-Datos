import numpy as np

class Pila:
    def __init__(self,cant=8):
        self.__arreglo = np.empty(cant,dtype=int)
        self.__topeA = 0
        self.__topeB = cant-1
        self.__cant = cant
        for i in range(cant):
            self.__arreglo[i] = 0

    def vacia(self,pila):
        if pila == 1:
            return self.__topeA == 0
        elif pila == 2:
            return self.__topeB == self.__cant
        else: print('\nPila incorrecta.')

    def completo(self):
        if self.__topeA == self.__topeB:
            return False

    def insertar(self,dato,pila):
        if self.completo() == False:
            print('\nArreglo lleno.')
        else:
            if pila == 1:
                self.__arreglo[self.__topeA] = dato
                self.__topeA += 1
            elif pila == 2:
                self.__arreglo[self.__topeB] = dato
                self.__topeB -=1
            else: print('\nNo existe esa pila.')

    def suprimir(self,pila):
        if not self.vacia(pila) and pila == 1:
            x = self.__arreglo[self.__topeA]
            self.__topeA -= 1
            return x
        elif not self.vacia(pila) and pila == 2:
            x = self.__arreglo[self.__topeB]
            self.__topeB += 1
        else:
            print('\nPila vacia o incorrecta.')

    def recorrer(self,pila):
        if not self.vacia(pila):
            if pila == 1:
                for i in range(self.__topeA):
                    print(self.__arreglo[i])
            elif pila == 2:
                for i in range(self.__topeB+1,len(self.__arreglo)):
                    print(self.__arreglo[i])