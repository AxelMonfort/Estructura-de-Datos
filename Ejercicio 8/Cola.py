
class Cola:
    __items= []
    __max= 0 #Cantidad máxima de elementos
    __pri= 0  #Primer elemento
    __ult= 0  #Último elemento
    __cant= 0 #Cantidad de elementos en un momento

    def __init__(self, xmax):
        self.__items= []
        self.__max= xmax
        self.__pri= 0
        self.__ult= 0
        self.__cant= 0

    def __str__(self):
        return f"{self.__items}"

    def Mostrar(self):
        print(self.__items)

    def Vacia(self):
        return self.__cant == 0

    def Llena(self):
        return self.__cant == self.__max

    def Insertar(self, dato):
        if not self.Llena():
            self.__items.insert(self.__ult, dato) #Insertamos en la última posición
            self.__ult= (self.__ult+1)%self.__max #Esto da 0 cuando el último y el máximo sean iguales osea que la cola está llena
            self.__cant += 1
        else:
            print("Cola llena")

    def Suprimir(self):
        if not self.Vacia():
            dato= self.__items[self.__pri]
            self.__pri= (self.__pri+1)%self.__max #Esto da 0 cuando ya no haya más gente en la cola
            self.__cant -= 1
        else:
            dato="Pila vacía"
        return dato
