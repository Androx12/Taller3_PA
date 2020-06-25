class Menus_Vistas:

    def __init__ (self): #Menús de vistas que se utilizan en el flujo como menús
        self.SaltoLinea =   ""

    def Inicio_Programa(self):
        print( self.SaltoLinea + "\n" + "\n" +"Bienvenido al Sistema del ICE")

    def Fin_Programa(self):
        print("************************************")
        print( "\n" + self.SaltoLinea + "Gracias por usar el Sistema del ICE")
        print("\n")
        print("************************************")


    def OpcionesMenu(self):
        print("")
        print("*----*----*----*----*----*----*----*")
        print("| 1. Presione 'C' para CONTINUAR.  |")
        print("| 2. Presione 'S' para SALIR.      |")
        print("*----*----*----*----*----*----*----*")
        print("")
    
    def DiezLineas(self):
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")