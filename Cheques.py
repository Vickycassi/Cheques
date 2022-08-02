import sys
import csv
from datetime import datetime

sys.argv
parametros = sys.argv[1]
nombre_archivo_csv = parametros[0]
salida = parametros[2]
tipo_cheque_a_filtrar = parametros[3]
estado_a_filtrar = None 
rango_fecha = None

if len(parametros)== 5:
    opcional = parametros[4]
    tipos_estado = ["PENDIENTE", "APROBADO", "RECHAZADO"]
    if opcional in tipos_estado:
        estado_a_filtrar = opcional 
    else: 
        rango_fecha = opcional.split(':')
        
elif len(parametros) == 6:
    estado_a_filtrar = parametros[4]
    rango_fecha = parametros[5].split(':')
    
if rango_fecha:
    rango_fecha_inicio = datetime.timestamp(datetime.strptime(rango_fecha[0], '%d-%m-%Y'))
    rango_fecha_fin = datetime.timestamp(datetime.strptime(rango_fecha[1], '%d-%m-%Y'))

res = []

with open(nombre_archivo_csv, 'r') as archivo_csv:
    csv_reader = csv.reader(archivo_csv, delimiter=',')
    for fila in csv_reader:
        dni = fila[8]
        tipo_cheque = fila[9]
        estado_cheque = fila[10]
        fecha = float(fila[6])
        if dni != dni_a_filtrar or tipo_cheque != tipo_cheque != tipo_cheque_a_filtrar:
            continue
        if estado_a_filtrar and estado_cheque != estado_cheque:
           continue
        if rango_fecha and (fecha < rango_fecha_inicio or fecha > rango_fecha_fin):
           continue 
        
        res.append(fila)

vistos = set()
for fila in res:
    nro_cheque = fila[0]
    nro_cuenta = fila[3]
    dni = fila[8]
    if (nro_cheque, nro_cuenta, dni) in vistos:
        res.append("Hay datos que se repiten en dos cheques")
    else:
        vistos.add((nro_cheque, nro_cuenta, dni))



if salida == "PANTALLA":
    for fila in res:
        print(fila)
elif salida == "CSV":
     datos_filtados = [[fila[3], fila[5], fila[6], fila[7]] for fila in res]
     dt = datetime.now()
     dt = dt.strftime("%d-%m-%Y")
     with open(f'{fila[8]}-{dt}.csv', 'w', newline='') as archivo_salida:
        writer= csv.writer(archivo_salida)
        writer.writerows(datos_filtados)

     

