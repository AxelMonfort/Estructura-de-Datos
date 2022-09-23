class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

    def getDerecha(self,referencia):
        self.derecha = referencia
    def getIzquierda(self,referencia):
        self.izquierda = referencia

    def setDato(self,dato):
        self.dato = dato
