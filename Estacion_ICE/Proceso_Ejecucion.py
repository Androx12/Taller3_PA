from Vistas_Menu import Menus_Vistas
from Operador.Operador_Control import Operador_Control
from SubEstacion.SubEstacion_Control import SubEstacion_Control
from Estacion.Estacion_Control import Estacion_Control
from BD import BD
import msvcrt

Obj_VistaMenu = Menus_Vistas()

class Ejecucion_Sistema_Control:

    Obj_VistaMenu = Menus_Vistas()
    Obj_OpControl = Operador_Control()
    Obj_SubEstControl = SubEstacion_Control ()
    Obj_EstacionControl = Estacion_Control()
    ObjBD = BD()

    def __init__(self):
        self.Obj_VistaMenu.Inicio_Programa()

    def CorrerPrograma(self):
        
        BanderaPrograma = True
        Entrada_Usuario = None

        while BanderaPrograma == True:  #Se crea un ciclo para mantener el flujo validando con (BanderaPrograma)

            try:
                print('Menu Sistema del ICE...')
                self.Obj_VistaMenu.OpcionesMenu() #Se trae la vista de el Menú
                Entrada_Usuario = input("Seleccione una opción de Menú --> ")
                
                if (Entrada_Usuario == 'C'): #Flujo en C

                    ValorBD = self.ObjBD.ProcesoDB() #Se llama al controlador del Proceso de BD (Retorna Lista)

                    if ValorBD: #Si ese retorno contiene valores en lista
                        self.Obj_VistaMenu.DiezLineas()
                        print('Bienvenido de nuevo: ', ValorBD)
                        self.Obj_SubEstControl.AgregarSubEstacion() #Solo se solicita la SubEstacion
                    else:
                        self.Obj_VistaMenu.DiezLineas()                   #Si no existe se llama el 'Control Operador'
                        Operador = [self.Obj_OpControl.AgregarOperador()] #y su retorno se guarda en una lista
                        CNX = self.ObjBD.SQLLite_Create_DB()        #Se abre la CNX a BD
                        self.ObjBD.Insertar_New_Row(CNX,Operador)   #Y se envía a guardar a BD el valor que retorno el Operador
                        self.Obj_SubEstControl.AgregarSubEstacion() #Se solicita la SubEstacion
                    self.Obj_EstacionControl.Continuar()
                    self.Obj_EstacionControl.ControlDatos()
                    self.Obj_EstacionControl.QuitarResumen()
                    
                else:
                    if Entrada_Usuario == 'S':  #Flujo en S
                        self.Obj_VistaMenu.DiezLineas()
                        self.Obj_VistaMenu.Fin_Programa() #Vista de Salida
                        BanderaPrograma = False
                    else:                       #Otra entrada genera un flujo de error para obligar al usuario
                        BanderaPrograma = True  #a ingresar los datos dentro del menú
                        self.Obj_VistaMenu.DiezLineas()
                        print('Entrada invalida.')
                        print("Las opciones del Menú son 'C' y 'S' (MAYÚSCULAS).")
                        print("Presione 'C' para voler al Menú")
                        key = None
                        while key != 'C':           #Hasta que no se presione 'C' no permite la entrada de datos
                            key = msvcrt.getwch()   #como un HANDLE de .Net
                        self.Obj_VistaMenu.DiezLineas()
            except:
                pass