from SubEstacion.SubEstacion_Modelo import SubEstacion_Modelo

class SubEstacion_Control:

    def __init__ (self):
        self.ListaSubEstaciones = []

    def AgregarSubEstacionLista(self, SubEstacion):
        self.ListaSubEstaciones.append(SubEstacion)

    def AgregarSubEstacion (self):
        try:
            print("\n")
            Bandera = True
            while Bandera == True:
                DatosNuevaSubEstacion = input("* Ingrese el nombre de la Sub Estación: --> \n")
                if DatosNuevaSubEstacion == "":
                    print("\n")
                    print("No puede ingresar un valor vacío")
                    print("\n")
                    Bandera = True
                else:
                    Bandera = False
                    NuevaSubEstacion = SubEstacion_Modelo(DatosNuevaSubEstacion)
                    return DatosNuevaSubEstacion
                    self.AgregarSubEstacionLista(NuevaSubEstacion)
        except:
            self.Vista.Msj("Error en la entrada del usuario") 