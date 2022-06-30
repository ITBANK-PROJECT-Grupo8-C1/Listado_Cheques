import csv
from sqlite3 import Timestamp
import sys
import datetime

#*********************DEFINICIONES DE FUNCIONES*********************

def obtenerListadoCompleto(lectura, dni, tipocheque, estadocheque, Fdesde, Fhasta):
    lista=[]
    for linea in lectura:
        if linea[-3] == dni and linea[-2] == tipocheque and linea[-1] == estadocheque:
            #faltaria agregar la comprobacion de las fechas, por ejemplo (Fdesde <= linea[-5] <= Fhasta)
            lista.append(linea)
    return lista

def obtenerListadoSinFecha(lectura, dni, tipocheque, estadocheque):
    lista=[]
    for linea in lectura:
        if linea[-3] == dni and linea[-2] == tipocheque and linea[-1] == estadocheque:
            lista.append(linea)
    return lista

def obtenerListadoSinEstado(lectura, dni, tipocheque, Fdesde, Fhasta):
    lista=[]
    for linea in lectura:
        if linea[-3] == dni and linea[-2] == tipocheque:
            #faltaria agregar la comprobacion de las fechas, por ejemplo (Fdesde <= linea[-5] <= Fhasta)
            lista.append(linea)
    return lista

def revisarError(listado): #devuelve booleano - 1 si no hay errores, 0 si hay errores.
    b=1
    for i, cheque in enumerate(listado):
        j=i+1
        while j <= len(listado) and b:
            if cheque[0] == listado[j][0]:
                b=0
            else:
                j+=1
    return b

def Salida(tipodesalida, listado, dni):
    if tipodesalida.upper() == "PANTALLA":
        for i, cheque in enumerate(listado):
            print("Cheque N° ",i,":",cheque)
    elif tipodesalida.upper() == "CSV":
        fecha_timestamp = str(datetime.now().timestamp())
        file = open(dni+"_"+fecha_timestamp+".csv", "w")#abro archivo para escribir.
        for cheque in listado:
            file.write(cheque[3]+","+cheque[5]+","+cheque[6]+","+cheque[7]+"\n") #escribimos cada linea del listado, con los datos pedidos.
    else:
        print("Hubo un error al cargar la salida.")

#*********************TOMA DE VARIABLES GLOBALES*********************

argumentos = sys.argv
#creo y leo el archivo csv
file = open("text.csv", "r")
Csv = csv.reader(file)
#tomo datos de argumentos obligatorios.
dni = argumentos[1]
salida = argumentos[2]
tipo = argumentos[3]

#*********************PUNTOS CRITICOS*********************

if len(argumentos)<4: #no se puede hacer nada, no estan los args "obligatorios"
    print("Hacen falta mas argumentos.")
elif len(argumentos) == 5: #verificar si es que esta el estado de cheque.
    if argumentos[4] == "PENDIENTE" or argumentos[4] == "APROBADO" or argumentos[4] == "RECHAZADO": #hacer filtro por estado de cheque
        estado = argumentos[4]
        listadoCheques = obtenerListadoSinFecha(Csv, dni, tipo, estado)
        Salida(salida, listadoCheques, dni)
    else: #no hacer filtro por estado de cheque
        fechaDesde = int(argumentos[5][:8])
        fechaHasta = int(argumentos[5][9:])
        listadoCheques = obtenerListadoSinEstado(Csv, dni, tipo, fechaDesde, fechaHasta)
        Salida(salida, listadoCheques, dni)
elif len(argumentos) == 6: #todos los parametros pasados.
    estado = argumentos[4]
    #falta hacer filtro por fecha.
    fechaDesde = int(argumentos[5][:8])
    fechaHasta = int(argumentos[5][9:])
    #guardo variables de los args.
    listadoCheques = obtenerListadoCompleto(Csv, dni, tipo, estado, fechaDesde, fechaHasta)
    # guardo el listado con los dni´s coincidentes
    #reviso errores.
    if revisarError(listadoCheques):#no hay errores, entonces continuo
        Salida(salida, listadoCheques, dni)
    else: #hay error, entonces finalizo con un mensaje de error
        print("ERROR. para el mismo DNI, se encuentran 2 o más cheques con el mismo identificador.")

