from Manejador_Viajero import ManejadorV

class MenuO:
    __opcion=None
    def __init__(self):
        self.__opcion=None

    def menuOpciones(self):
        manej = ManejadorV()
        manej.readFile()
        manej.comparacion()
        # usuario = input("\n Ingrese numero de viajero:")
        # j = manej.busqpersona(usuario)
        # print("\n 1--Consultar cantidad de Millas-- ")
        # print("\n 2--Acumular Millas--")
        # print("\n 3--Canjear Millas--")
        # print("\n 0-- Salir--")
        # self.__opcion = input("\n Seleccione una opcion: ")
        # if self.__opcion == '1':
        #         print("\n La cantidad de millas acumuladas es de: ",manej.MostrarMillas(j))
        # elif self.__opcion == '2':
        #         acum = float(input("\n Ingrese cantidad de millas a acumular: "))
        #         manej.millas_Acum(j,acum)
        #         print("\nCantidad total de millas acumuladas: ",manej.MostrarMillas(j))
                
        # elif self.__opcion == '3':
        #         pass
        # elif self.__opcion == '0':
        #         print("Programa Terminado")
        # elif self.__opcion >= '4':
        #         print("Número incorrecto, ingrese nuevamente.\n")
        #         return self.menuOpciones()    
        # elif self.__opcion >= '5':
        #         manej.mostrar()