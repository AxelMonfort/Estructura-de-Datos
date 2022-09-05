from Cola import Cola
import random

if __name__ == '__main__':
    Cola=Cola()
    max= 0 #Máximo tiempo de espera
    TAC=int(input("Ingrese el tiempo de atención del cajero en minutos:  "))
    FLCC=int(input("Ingrese la frecuencia de llegada de los clientes a la cola en minutos:  "))
    TAT=int(input("Ingrese el tiempo de atención en total del cajero en minutos:  "))
    cajero=0 #Si el cajero está desocupado, la variable cajero tendrá el valor 0
    #contc=0 #Contador de clientes -> no lo uso

    for i in range(TAT):
        x=random.randint(0, FLCC) #Genera un número aleatorio entre 0 y la frecuencia de llegada de los clientes
        if x == 1: #Cuando "toca" 1 es porque llegó un nuevo cliente
            Cola.Insertar(i)
            #contc += 1 -> no lo uso, cambié el contador de clientes por i
        if cajero == 0:
            if not Cola.Vacia():
                cliente= Cola.Suprimir()
                TEC= i-cliente #Tiempo de espera del cliente
                if max < TEC:
                    max= TEC
                cajero= TAC
        else:
            cajero= cajero-1
    print("El tiempo máximo de espera fué: {} minutos" .format(max))


