from SubEstacion.SubEstacion_Modelo import SubEstacion_Modelo

class SubEstacion_Control:

    def __init__ (self):
        self.ListaSubEstaciones = []

    def AgregarSubEstacionLista(self, SubEstacion):
        self.ListaSubEstaciones.append(SubEstacion)

    def AgregarSubEstacion (self):
        try:
            print("\n")
            DatosNuevaSubEstacion = input("* Ingrese el nombre de la Sub Estación: --> \n")
            NuevaSubEstacion = SubEstacion_Modelo(DatosNuevaSubEstacion)
            self.AgregarSubEstacionLista(NuevaSubEstacion)
        except:
            self.Vista.Msj("Error en la entrada del usuario") 