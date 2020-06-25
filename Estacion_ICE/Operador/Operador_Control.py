from Operador.Operador_Modelo import Operador_Modelo

class Operador_Control:

    Operador = 'Vacio'

    def __init__ (self):
        self.ListaOperadores = []

    def AgregarOperadorLista(self, Operador):   #Metodo que agrega elementos a la lista de la clase
        self.ListaOperadores.append(Operador)
        self.Operador = self.ListaOperadores[0]

    def AgregarOperador (self):     
        try:
            print("\n")
            DatosNuevoOperador = input("* Ingrese el nombre del Operador: --> \n") #Se solicita entrada al Usuario
            print("\n")
            print("\n")
            NuevoOperador = Operador_Modelo(DatosNuevoOperador) #Se envia a la clase Modelo Operador
            self.AgregarOperadorLista(NuevoOperador)    #Se ejecuta el metodo para agregarlo a lista
            return DatosNuevoOperador   #Retorna el valor que se ingreso como str pero afuera se trasforma a list
        except:
            print("Error en la entrada del usuario") 

