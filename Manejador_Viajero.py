from claseViajeroF import Viajero
import csv

class ManejadorV:
    __lista = []
    def __init__(self):
         self.__lista = []
         
    def readFile(self):
        archivo = open("viajerosFrecuentes.csv")
        reader = csv.reader (archivo, delimiter=',')
        for fila in reader:
            viajerosN = Viajero(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.__lista.append(viajerosN)
        archivo.close()
    
    def busqpersona(self, usuario):
        flag = False
        i = 0
        while ((i<= len(self.__lista)) & (flag == False)):
            if self.__lista[i].getnumviajero() == usuario:
                flag = True
                j = i
            i+=1
        if flag == False:
            print("El numero de pasajero no es correcto")
        elif flag == True:
            return (j)
    
    def MostrarMillas(self, j):
        return self.__lista[j].getMillas()
    
    def millas_Acum(self, j, acum):
        self.__lista[j].acumularMillas(acum)
    
    def mostrar (self):
        for i in range (len(self.__lista)):
            if self.__lista[i].getMillas()>self.__lista[i+1].getMillas():
                print(self.__lista.getnumviajero())

    def comparacion(self):
        print("Se realiza comparacion de cantidad de milla acumuladas con el numero 1000")
        for i in range(len(self.__lista)+1):
            print("El viajero {} tiene {} millas acumuladas".format(self.__lista[i].getnombre(), self.__lista[i].getMillas()))
            if self.__lista[i].getMillas()>self.__lista[i+1].getMillas():
                print (self.__lista[i].getnombre())
            else: print(self.__lista[i+1].getnombre())
    
    otroViajero=Viajero('2','32435212','Alekas','perez',4000)
    if otroViajero==self.__lista[num-1]:
        print('El viajero 2 --tiene las mismas-- millas que el viajero 1')
    else:
        print('El viajero 1 --no tiene las mismas-- millas que el viajero 2')
    otroViajero=300+otroViajero
    print(otroViajero.canttotalmillas())
    otroViajero=100-otroViajero
    print(otroViajero.canttotalmillas())
    

        
        
#def canjearMillas(self, cMillas):
        #if cMillas <= self.__millas:
            
            #elif: print("Error en la operacion.")
    #def busqViajero(self, usuario, lista):
