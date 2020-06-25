from Vistas_Menu import Menus_Vistas
from Operador.Operador_Control import Operador_Control

Obj_VistaMenu = Menus_Vistas()

class Ejecucion_Sistema_Control:

    Obj_VistaMenu = Menus_Vistas()
    Obj_OpControl = Operador_Control()

    def __init__(self):
        self.Obj_VistaMenu.Inicio_Programa()

    def CorrerPrograma(self):
        
        BanderaPrograma = True
        Entrada_Usuario = None

        while BanderaPrograma == True:

            try:
                if(Entrada_Usuario == None):

                    Entrada_Usuario = input('Para REGISTRAR presione "C" para salir presione "S" \n')

                    if (Entrada_Usuario == 'C'):

                        self.Obj_OpControl.AgregarOperador()
                        
                    else:
                        Obj_VistaMenu.Fin_Programa()
                        BanderaPrograma = False
                else:
                    Obj_VistaMenu.Fin_Programa()
                    BanderaPrograma = False
            except:
                pass