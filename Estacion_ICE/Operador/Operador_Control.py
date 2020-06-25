from Operador.Operador_Modelo import Operador_Modelo

class Operador_Control:

    def __init__ (self):
        self.ListaOperadores = []

    def AgregarOperador(self, Operador):
        self.ListaOperadores.append(Operador)

    def AgregarOperador (self):
        try:
            DatosNuevoOperador = input("Ingrese el nombre del Operador")
            NuevoOperador = Operador_Modelo(DatosNuevoOperador)
            self.AgregarOperador(NuevoOperador)
        except:
            self.Vista.Msj("Error en la entrada del usuario") 

