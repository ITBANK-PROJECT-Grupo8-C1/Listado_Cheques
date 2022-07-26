# Listado_Cheques

## Problemática 
Se quiere poder consultar los cheques que tiene emitidos y depositados en sus 
cuentas un determinado cliente, pudiendo estar estos pendientes, aprobado o 
rechazado.
Para esto la problemática a resolver es que se tiene que obtener la información 
desde un archivo
Por lo que dado un script en Python se solicita que se puedan ingresar las 
siguientes acciones por línea de comando y se visualicen los resultados por 
pantalla.

## Requerimientos específicos 
* 1. El script de Python se debe llamar listado_chesques.py
* 2. El orden de los argumentos son los siguientes: 
    a. Nombre del archivo csv.
    b. DNI del cliente donde se filtraran.
    c. Salida: PANTALLA o CSV
    d. Tipo de cheque: EMITIDO o DEPOSITADO
    e. Estado del cheque: PENDIENTE, APROBADO, RECHAZADO. (Opcional)
    f. Rango fecha: xx-xx-xxxx:yy-yy-yyyy (Opcional)
* 3. Si para un DNI dado un número de cheque de una misma cuenta se repite se 
debe mostrar el error por pantalla, indicando que ese es el problema.
* 4. Si el parámetro “Salida” es PANTALLA se deberá imprimir por pantalla todos
los valores que se tienen, y si “Salida” es CSV se deberá exportar a un csv 
con las siguientes condiciones:
    a. El nombre de archivo tiene que tener el formato <DNI><TIMESTAMPS ACTUAL>.csv
    b. Se tiene que exportar las dos fechas, el valor del cheque y la cuenta.
* 5. Si el estado del cheque no se pasa, se deberán imprimir los cheques sin 
filtrar por estado

## Ejemplos de uso
* py nombreArchivo NombreCSV.csv dni salida tipo estado rangoFecha(formato:xx-xx-xxxx:yy-yy-yyyy)

* py listado_cheques.py test.csv 23665789 CSV EMITIDO 4-4-2021:4-5-2021

* py listado_cheques.py test.csv 23665789 PANTALLA RECHAZADO 4-4-2021:4-4-2021
