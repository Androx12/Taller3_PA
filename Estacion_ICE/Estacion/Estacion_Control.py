from .Estacion_Vistas import Estacion_Vistas
import msvcrt
import csv

class Estacion_Control:

    def __init__(self): #Creamos 3 diccionarios para el control de los datos
        self.Horas_Ciudades = {}
        self.Consumo_Ciudades = {}
        self.Consumo_Total_Ciudad = {}
        self.ListaTotal = []
        self.ObjEstacionVistas = Estacion_Vistas()


    def ConteoCiudades(self):
        #Abrimos el archivo y separamos por ';' en un objeto reader, guarda cada linea del archivo como lista
        with open('mediciones.csv') as Archivo:
            Lector = csv.reader(Archivo, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
            
            for fila in Lector:
                self.ListaTotal.append(fila[1]) #Llenamos la lista con todas los Id de ciudades (fila[1])
            
            QuitarRepetidos = list( dict.fromkeys(self.ListaTotal)) #Quitamos los repetidos
        #Creamos una variable que nos ayudará a contar cuantas ciudades hay en el archivo
        Cantidad = 0
        for contenido  in QuitarRepetidos:
            Cantidad = Cantidad + 1
        return Cantidad


    def ControlDatos(self):
        #Abrimos el archivo y separamos por ';' en un objeto reader, guarda cada linea del archivo como lista
        with open('mediciones.csv') as Archivo:
            Lector = csv.reader(Archivo, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
            
            #Teniendo cada linea como una lista, podemos clasificar los elementos
            for fila in Lector:
                #Los valores son (Id -> fila[1]) (Hora -> fila[0]) (Consumo -> fila[2]))

                #Preguntamos si el Id existe en cualquiera de los diccionarios
                if fila[1] in self.Horas_Ciudades:

                    #En caso de que exista creamos un valor acumulado que será el valor
                    #de consumo guardado (Consumo_Ciudades[fila[1]]) + el nuevo consumo (fila[2])
                    ConsumoTotal = float(fila[2]) + float(self.Consumo_Ciudades[fila[1]])

                    #Se valida si el consumo nuevo es mayor al consumo guardado para realizar un cambio

                    if(float(fila[2]) > float(self.Consumo_Ciudades[fila[1]])): #En caso de ser mayor

                        self.Consumo_Ciudades[fila[1]] = fila[2]    #Se cambia el consumo mayor para esa ciudad (fila[1])
                        self.Horas_Ciudades[fila[1]] = fila[0]      #Se cambia la hora de mayor consumo para esa ciudad (fila[1])
                        self.Consumo_Total_Ciudad[fila[1]] = ConsumoTotal   #Se modifica el consumo total con la suma anterior
                    else:
                        #En caso de ser menor solo modifica el consumo total con la suma anterior
                        self.Consumo_Total_Ciudad[fila[1]] = ConsumoTotal
                else: #En caso de que no exista se agragan los valores a los diccionarios donde el KEY es el Id de ciudad

                    self.Consumo_Ciudades[fila[1]] = fila[2]
                    self.Horas_Ciudades[fila[1]] = fila[0]
                    self.Consumo_Total_Ciudad[fila[1]] = fila[2]
        for Key in self.Horas_Ciudades:
            print("")
            print("Ciudad: ", Key)
            print("Mayor hora de consumo: {} (Formato 24h) con un total para esa hora: {} KW".format(self.Horas_Ciudades[Key], self.Consumo_Ciudades[Key]))
            print("Consumo acumulado en KW de ciudad: ", self.Consumo_Total_Ciudad[Key])
            print("")
            print("--------------------------------------------------")

    def Continuar(self):
        print("--------------------------------------------------")
        print("El documento a revisar registra un conteo de {} ciudades.".format(self.ConteoCiudades()))
        print("")
        print("Presiones 'C' para realizar el estudio.")
        key = None
        while key != 'C':           #Hasta que no se presione 'C' no permite la entrada de datos
            key = msvcrt.getwch()   #como un HANDLE de .Net
        self.ObjEstacionVistas.DiezLineas()


    def QuitarResumen(self):
        print("")
        print("El resumen se detalle en las lineas de arriba")
        print("")
        print("Presiones 'C' para volver al menú del sistema.")
        key = None
        while key != 'C':           #Hasta que no se presione 'C' no permite la entrada de datos
            key = msvcrt.getwch()   #como un HANDLE de .Net
        self.ObjEstacionVistas.DiezLineas()
       