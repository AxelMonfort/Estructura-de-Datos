from claseNodo import Nodo

class Arbol:
    def __init__(self,dato):
        self.__raiz = Nodo(dato)

    def __agregarRecursivo(self,nodo,dato):
        if dato != nodo.dato:
            if dato < nodo.dato:
                if nodo.izquierda is None:
                    nodo.izquierda = Nodo(dato)
                else:
                    self.__agregarRecursivo(nodo.izquierda,dato)
            else:
                if nodo.derecha is None:
                    nodo.derecha = Nodo(dato)
                else:
                    self.__agregarRecursivo(nodo.derecha,dato)
        else:
            print('\nError, ya hay un dato igual.')

    def __inOrden(self,nodo):
        if nodo != None:
            self.__inOrden(nodo.izquierda)
            print(nodo.dato, end=" ")
            self.__inOrden(nodo.derecha)

    def __preOrden(self,nodo):
        if nodo != None:
            print(nodo.dato,end=" ")
            self.__preOrden(nodo.izquierda)
            self.__preOrden(nodo.derecha)

    def __postOrden(self,nodo):
        if nodo != None:
            self.__postOrden(nodo.izquierda)
            self.__postOrden(nodo.derecha)
            print(nodo.dato, end=" ")

    def __buscar(self,nodo,elemento):
        if nodo is None:
            return None
        if nodo.dato == elemento:
            return nodo
        if nodo.dato > elemento:
            return self.__buscar(nodo.izquierda,elemento)
        else:
           return self.__buscar(nodo.derecha,elemento)

    def __Nivel(self,nodo,elemento,cont):
        if nodo is None:
            return None
        if nodo.dato == elemento:
            return cont + 1
        if elemento < nodo.dato:
            return self.__Nivel(nodo.izquierda,elemento,cont + 1)
        else:
            return self.__Nivel(nodo.derecha,elemento,cont + 1)

    def __Hoja(self,elemento):
        nodo = self.Buscar(elemento)
        if (nodo.izquierda and nodo.derecha) == None:
            print('\nEl elemento ',elemento,' es una hoja.')
        else: print('\nNo es una hoja.')

    def __Altura(self,nodo):
        if nodo == None:
            return 0
        else:
            return 1 + max(self.__Altura(nodo.izquierda), self.__Altura(nodo.derecha))

    def __Hijo(self,hijo,padre):
        nodo = self.Buscar(padre)
        if (nodo.izquierda.dato or nodo.derecha.dato) == hijo:
            print('\n' f"El dato {hijo} es hijo de {padre}.")
        else: print('\n No es hijo.')

    def __Camino(self,nodo,elemento):
        if nodo is not None:
            if nodo.dato < elemento:
                print('\n' f"Camino {nodo.dato}")
                return self.__Camino(nodo.derecha,elemento)
            else: print('\n' f"Camino {nodo.dato}");return self.__Camino(nodo.izquierda,elemento)
        else:print('\n No se encuentra el camino para ese dato.')

    def __Suprimir(self,elemento):
        nodo,ubicacion,padre = self.__buscarSuprimir(self.__raiz,elemento)
        if nodo is not None:
            if (nodo.izquierda and nodo.derecha) == None:    #En el caso que sea una hoja.
                if ubicacion == 'i':
                    padre.getIzquierda(None)
                else: padre.getDerecha(None)
            if nodo.derecha != None and nodo.izquierda == None:  #Nodo a eliminar tiene hijo Derecho
                padre.getDerecha(nodo.derecha)
            elif nodo.derecha == None and nodo.izquierda != None:  #Nodo a eliminar tiene hijo Izquierdo
                padre.getIzquierda(nodo.izquierda)
            if (nodo.derecha and nodo.izquierda) != None:   #Nodo a eliminar tiene dos hijos.
                nodoIzquierdo = self.__Izquierda(nodo)
                aux = nodoIzquierdo
                self.__Suprimir(aux.dato)
                nodo.setDato(nodoIzquierdo.dato)
        else: print('\nDato invalido.')

    def __Izquierda(self,nodo):
        if nodo != None:
            if (nodo.derecha and nodo.izquierda) == None:
                return nodo
            else:
                return self.__Izquierda(nodo.izquierda)

    def __buscarSuprimir(self,nodo,elemento,ubicacion=None,padre=None):
        if nodo is None:
            return None
        if nodo.dato == elemento:
            return nodo,ubicacion,padre
        if nodo.dato > elemento:
            return self.__buscarSuprimir(nodo.izquierda,elemento,'i',nodo)
        else:
           return self.__buscarSuprimir(nodo.derecha,elemento,'d',nodo)




    #Funciones Publicas

    def Agregar(self,dato):
        self.__agregarRecursivo(self.__raiz,dato)

    def InOrden(self):
        print('\n--------Árbol INORDEN--------')
        self.__inOrden(self.__raiz)

    def PostOrden(self):
        print('\n-----------Árbol POSTORDEN---------')
        self.__postOrden(self.__raiz)

    def PreOrden(self):
        print('\n-----------Árbol PREORDEN----------')
        self.__preOrden(self.__raiz)

    def Buscar(self,elemento):
        return self.__buscar(self.__raiz,elemento)

    def Nivel(self,elemento):
        return self.__Nivel(self.__raiz,elemento,0)

    def Hoja(self,elemento):
        return self.__Hoja(elemento)

    def Altura(self):
        return self.__Altura(self.__raiz)

    def Hijo(self,hijo,padre):
        self.__Hijo(hijo,padre)

    def Camino(self,elemento):
        self.__Camino(self.__raiz,elemento)

    def Suprimir(self,elemento):
        self.__Suprimir(elemento)