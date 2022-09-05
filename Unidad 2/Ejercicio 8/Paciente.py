class Paciente:
    __nombre=""
    __DNI= 0
    __Especializacion= 0 #Un código del 1 al 4
    __Llegada= 0 #Tiempo de llegada en minutos


    def __init__(self, dni, esp, tim):
        self.__nombre= "PRUEBA"
        self.__DNI= dni
        self.__Especializacion= esp
        self.__Llegada= tim

    def __str__(self):
        return f"{self.__nombre}, {self.__DNI}, {self.__Especializacion}, {self.__Llegada}"

    def getNombre(self):
        return self.__nombre
    def getDNI(self):
        return self.__DNI
    def getEspecializacion(self):
        return self.__Especializacion
    def getLlegada(self):
        return self.__Llegada
