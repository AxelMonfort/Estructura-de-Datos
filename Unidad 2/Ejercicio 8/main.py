from Cola import Cola
from ColaE import ColaE
from Paciente import Paciente
import random
if __name__ == '__main__':
    print("-------COMIENZA SIMULACIÓN-------")
    print("...")
    print("...")
    print("...")
    #Creación de colas de cada especialidad
    ColaGin= Cola(10) #Código Ginecologo = 1
    ColaCli= Cola(10) #Código Clínica = 2
    ColaOft= Cola(10) #Código Oftalmólogo = 3
    ColaPed= Cola(10) #Código Pediatra = 4
    ColaPacientes= ColaE() #Cola general de pacientes

    Simulacion= 4*60 #El total de horas que se atiende
    AtencionMedico= 20 #El tiempo que atiende cada médico a los pacientes
    ContPacientes= 0 #Contador de la cantidad de pacientes que les dieron turno
    sumaLlegada=0 #Para sacar el promedio
    i=1
    TotalPacientes=60 #Si entra un paciente cada 1 minuto, entonces serán 60 pacientes
    contG=0 #Contador de los pacientes que se atienden en Ginecología
    contC=0 #Contador de los pacientes que se atienden en la Clínica
    contO=0 #Contador de los pacientes que se atienden en Oftamología
    contP=0 #Contador de los pacientes que se atienden en Pediatría
    TiempoEsperaG=0 #Para sacar el promedio de tiempo Ginecología
    TiempoEsperaC=0 #Para sacar el promedio de tiempo Clínica
    TiempoEsperaO=0 #Para sacar el promedio de tiempo Oftalmólogo
    TiempoEsperaP=0 #Para sacar el promedio de tiempo Pediatría


    while i < 60:
        alea= random.randint(0, 1)
        if alea == 0: #Esto quiere decir si le pudo dar turno a un paciente, es decir se simula si por ejemplo el secretario se demoró mucho dando el turno y no pudo darle turno a las 60 personas que llegan
            #a
            dni= random.randint(30000000, 50000000)
            esp= random.randint(1, 4)
            tiempollegada= i
            sumaLlegada += tiempollegada
            Pacient= Paciente(dni, esp, tiempollegada)
            ColaPacientes.Insertar(Pacient)
            ContPacientes+=1
        i+=1

    while i < Simulacion:
        if not ColaPacientes.Vacia():
            unPaciente=ColaPacientes.Suprimir() #Tomamos un paciente de la cola de pacientes
            cod=unPaciente.getEspecializacion() #El código para saber a que cola llevarlo
            if cod == 1:
                if not ColaGin.Llena():
                    contG+=1
                    TiempoEsperaG=i-unPaciente.getLlegada() + AtencionMedico #Para saber el tiempo de espera aproximado
                    ColaGin.Insertar(unPaciente)
            elif cod == 2:
                if not ColaCli.Llena():
                    contC+=1
                    TiempoEsperaC=i-unPaciente.getLlegada() + AtencionMedico #Para saber el tiempo de espera aproximado
                    ColaCli.Insertar(unPaciente)
            elif cod == 3:
                if not ColaOft.Llena():
                    contO+=1
                    TiempoEsperaO=i-unPaciente.getLlegada() + AtencionMedico #Para saber el tiempo de espera aproximado
                    ColaOft.Insertar(unPaciente)
            elif cod == 4:
                if not ColaPed.Llena():
                    contP+=1
                    TiempoEsperaP=i-unPaciente.getLlegada() + AtencionMedico #Para saber el tiempo de espera aproximado
                    ColaPed.Insertar(unPaciente)
        i+=1


    promedioColaPaciente=sumaLlegada//ContPacientes #El promedio en la cola de turnos
    print("-------SIMULACIÓN COMPLETA-------")
    print("El promedio en la cola de turnos es: {} minutos".format(promedioColaPaciente))
    print("La cantidad de pacientes que se quedaron sin turno son: {}".format(TotalPacientes-ContPacientes))
    print("El promedio de espera en el Ginecólogo es de: {} minutos" .format(TiempoEsperaG//contG))
    print("El promedio de espera en la Clínica es de: {} minutos" .format(TiempoEsperaC//contC))
    print("El promedio de espera en el Oftalmólogo es de: {} minutos" .format(TiempoEsperaO//contO))
    print("El promedio de espera en el Pediatra es de: {} minutos" .format(TiempoEsperaP//contP))
