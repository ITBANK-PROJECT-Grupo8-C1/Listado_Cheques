# Listado_Cheques

Dado este tipo de archivo se sabe que contiene los siguientes campos con la 
siguiente información:
NroCheque: Número de cheque, este debe ser único por cuenta.
CodigoBanco: Código numérico del banco, entre 1 y 100.
CodigoScurusal: Código numérico de la sucursal del banco va entre 1 y 300.
NumeroCuentaOrigen: Cuenta de origen del cheque.
NumeroCuentaDestino: Cuenta donde se cobra el cheque.
Valor: float con el valor del cheque.
FechaOrigen: Fecha de emisión: (En timestamp)
FechaPago: Fecha de pago o cobro del cheque (En timestamp)
DNI: String con DNI del cliente donde se permite identificarlo
Estado: Puede tener 3 valores pendiente, aprobado o rechazado.

# Problemática 
Se quiere poder consultar los cheques que tiene emitidos y depositados en sus 
cuentas un determinado cliente, pudiendo estar estos pendientes, aprobado o 
rechazado.
Para esto la problemática a resolver es que se tiene que obtener la información 
desde un archivo
Por lo que dado un script en Python se solicita que se puedan ingresar las 
siguientes acciones por línea de comando y se visualicen los resultados por 
pantalla.

##Requerimientos específicos 
1. El script de Python se debe llamar listado_chesques.py
2. El orden de los argumentos son los siguientes: 
a. Nombre del archivo csv.
b. DNI del cliente donde se filtraran.
c. Salida: PANTALLA o CSV
d. Tipo de cheque: EMITIDO o DEPOSITADO
e. Estado del cheque: PENDIENTE, APROBADO, RECHAZADO. (Opcional)
f. Rango fecha: xx-xx-xxxx:yy-yy-yyyy (Opcional)
3. Si para un DNI dado un número de cheque de una misma cuenta se repite se 
debe mostrar el error por pantalla, indicando que ese es el problema.
4. Si el parámetro “Salida” es PANTALLA se deberá imprimir por pantalla todos
los valores que se tienen, y si “Salida” es CSV se deberá exportar a un csv 
con las siguientes condiciones:
a. El nombre de archivo tiene que tener el formato 
<DNI><TIMESTAMPS ACTUAL>.csv
b. Se tiene que exportar las dos fechas, el valor del cheque y la cuenta.
5. Si el estado del cheque no se pasa, se deberán imprimir los cheques sin 
filtrar por estado
