import csv
import sys
import time
from datetime import datetime

#*********************DEFINICIONES DE FUNCIONES*********************

def obtenerListadoCompleto(lectura, dni, tipocheque, estadocheque, rango):
    lista=[]
    for linea in lectura:
        if linea[-3] == dni and linea[-2] == tipocheque and linea[-1] == estadocheque and linea[-5] == rango[0] and linea[-4] == rango[1]:
            if rango[0] <= linea[-5] <= rango[1]:
                lista.append(linea)
            else:
                print("El cheque que está buscando no se encuentra dentro de las fechas pautadas.")
    return lista

def obtenerListadoSinFecha(lectura, dni, tipocheque, estadocheque):
    lista=[]
    for linea in lectura:
        if linea[-3] == dni and linea[-2] == tipocheque and linea[-1] == estadocheque:
            lista.append(linea)
    return lista

def obtenerListadoSimple(lectura, dni, tipocheque):
    lista=[]
    for linea in lectura:
        if linea[-3] == dni and linea[-2] == tipocheque:
            lista.append(linea)
    return lista

def obtenerListadoSinEstado(lectura, dni, tipocheque, rango):
    lista=[]
    for linea in lectura:
        if linea[-3] == dni and linea[-2] == tipocheque and linea[-5] == rango[0] and linea[-4] == rango[1]:
            if rango[0] <= linea[-5] <= rango[1]:
                lista.append(linea)
            else:
                print("El cheque que está buscando no se encuentra dentro de las fechas pautadas.")
    return lista

def verificarEstado(estadoCheque):
    return estadoCheque == 'PENDIENTE' or estadoCheque == 'APROBADO' or estadoCheque == 'RECHAZADO'

def convertirFecha(fechaDesde, fechaHasta):
    rango = []
    fechaDesde = int(time.mktime(datetime.datetime.strptime(fechaDesde, "%d-%m-%Y").timetuple()))
    fechaHasta = int(time.mktime(datetime.datetime.strptime(fechaHasta, "%d-%m-%Y").timetuple()))
    rango.append(fechaDesde)
    rango.append(fechaHasta)
    return rango

def revisarError(listado): #devuelve booleano.
    b=True
    for i, cheque in enumerate(listado):
        j=i+1
        while j <= len(listado) and b:
            if cheque[0] == listado[j][0]:
                b=False
            else:
                j+=1
    return b

def Salida(tipodesalida, listado, dni):
    if tipodesalida.upper() == "PANTALLA":
        for i, cheque in enumerate(listado):
            print("Cheque N° ",i,":",cheque)
    elif tipodesalida.upper() == "CSV":
        fecha_timestamp = datetime.now().strftime("%d/%m/%Y")
        file = open(dni+"_"+fecha_timestamp+".csv", "w") #abro archivo para escribir.
        # file = open("C:\Users\Karen\Desktop\tomi-sprint4\Listado_Cheques\test.csv")
        for cheque in listado:
            file.write(cheque[3]+","+cheque[5]+","+cheque[6]+","+cheque[7]+"\n") #escribimos cada linea del listado, con los datos pedidos.
    else:
        print("Hubo un error al cargar la salida.")

#*********************TOMA DE VARIABLES GLOBALES*********************

argumentos = sys.argv

#creo y leo el archivo csv
archivoCSV = argumentos[1]
file = open(archivoCSV, "r")
lineas = csv.reader(file)

#tomo datos de argumentos obligatorios.
dni = argumentos[2]
salida = argumentos[3]
tipo = argumentos[4]

#*********************PUNTOS CRITICOS*********************

if len(argumentos)<4: #no se puede hacer nada, no estan los args "obligatorios"
    print("Hacen falta mas argumentos.")

elif len(argumentos) == 4:
    listadoCheques = obtenerListadoSimple(lineas, dni, tipo)
    Salida(salida, listadoCheques, dni)

elif len(argumentos) == 5: #verificar si es que esta el estado de cheque.

    if verificarEstado(argumentos[5]): #hacer filtro por estado de cheque
        estado = argumentos[5]
        listadoCheques = obtenerListadoSinFecha(lineas, dni, tipo, estado)
        Salida(salida, listadoCheques, dni)

    else: #no hacer filtro por estado de cheque
        fechaDesde = int(argumentos[5][:8])
        fechaHasta = int(argumentos[5][9:])
        listadoCheques = obtenerListadoSinEstado(lineas, dni, tipo, convertirFecha(fechaDesde, fechaHasta))
        Salida(salida, listadoCheques, dni)

elif len(argumentos) == 6: #todos los parametros pasados.
    estado = argumentos[4]
    fechaDesde = int(argumentos[6][:8])
    fechaHasta = int(argumentos[6][9:])
    #guardo variables de los args.
    listadoCheques = obtenerListadoCompleto(lineas, dni, tipo, estado, convertirFecha(fechaDesde, fechaHasta))
    # guardo el listado con los dni´s coincidentes

    #reviso errores.
    if revisarError(listadoCheques):#no hay errores, entonces continuo
        Salida(salida, listadoCheques, dni)
    else: #hay error, entonces finalizo con un mensaje de error
        print("ERROR. Para el mismo DNI, se encuentran 2 o más cheques con el mismo número.")

