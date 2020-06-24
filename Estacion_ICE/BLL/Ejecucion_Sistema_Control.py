from ..PL.Menus_Vistas import Menus_Vistas

class Ejecucion_Sistema_Control:

    def __init__(self):
        self.VistasMenu = Menus_Vistas()
        self.VistasMenu.Inicio_Programa()

    def CorrerPrograma(self):
        print("Corriendo")






        """
        BanderaPrograma = True
        Entrada_Usuario = None

        while BanderaPrograma == True:

            try:
                if(Entrada_Usuario == None):

                    Entrada_Usuario = input('Para REGISTRAR presione C para salir presione S \n')
                    if (Entrada_Usuario == 'C'):
                        BanderaPrograma = True
                    else:
                        BanderaPrograma = False
                        #self.DetenerPrograma()
                else:
                    Entrada_Usuario = input('Registre el nombre del Operador \n')
                    BanderaPrograma = False
                    #self.DetenerPrograma()
            except:
                pass

    def DetenerPrograma (self):
        self.VistasMenu = Menus_Vistas()
        self.VistasMenu.Fin_Programa()
        """

    