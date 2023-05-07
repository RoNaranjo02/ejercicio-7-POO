import math

class Viajero:
    __num_viajero = ""
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum = ""
    
    def __init__(self,num_viajero="",dni="",nombre="",apellido="",millas_acum=""):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido =apellido
        self.__millas_acum = millas_acum
    
    def __str__(self):
        return 'Numero de viajero: {} Dni: {} Nombre: {} Apellido: {} Millas acumuladas: {}'.format(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum)
    
    def geDni(self):
        return self.__dni
    
    def getApellido(self):
        return self.__apellido
    
    def getMillas(self):
        return self.__millas_acum
    
    def getnumviajero(self):
        return self.__num_viajero
    
    def getnombre(self):   
        return self.__nombre
    
    def acumularMillas(self, acum):
        self.__millas_acum = self.__millas_acum + acum
    
    def __gt__(self,otro):
        if isinstance(otro, Viajero):
            return self.__millas_acum < otro.__millas_acum
        elif isinstance(otro, int):
            return self.__millas_acum < otro
    def __add__(self,otro):
        if type(otro) == Conjunto:
            conjunto1 = self.__ListaNumeros
            conjunto2 = otro.getConjunto()
            for i in range(len(conjunto2)):
                if conjunto2[i] not in conjunto1:
                    conjunto1.append(conjunto2[i])

            return conjunto1
    
    def __sub__(self,otro):
        if type(otro) == Conjunto:
            ConjuntoDiferencia = []
            for i in range(len(self.__ListaNumeros)):
                if self.__ListaNumeros[i] not in otro.getConjunto():
                    ConjuntoDiferencia.append(self.__ListaNumeros[i])
            return ConjuntoDiferencia
    
    def __eq__(self,otro):
        if type(otro) == Conjunto:
            bandera = True
          
            conjunto1 = self.__ListaNumeros
            conjunto2 = otro.getConjunto()
            
            if(len(conjunto1) == len(conjunto2)):
                
                i = 0
                while i < len(conjunto1) and bandera == True:
                    if conjunto1[i] not in conjunto2:
                        bandera = False
                    i+=1
                
            else:
                bandera = False
            
            return bandera
            
            
        
    
         

