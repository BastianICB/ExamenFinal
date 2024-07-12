#import estatitics geometryc_mean media geometrica
import statistics as est
import random as rd
import csv

trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez',
                'Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']

def asignar_sueldos_aleatorios(lista_trabajadores):
    for i in trabajadores:
        sueldos =rd.randint(300000,2500000)
        lista_trabajadores.append({
            'Nombre' : i,
            'Sueldo' : sueldos
        })
    print(lista_trabajadores)

def clasificar_sueldos(lista_trabajadores):
    total_sueldos = 0
    contador = 0
    contador2 = 0
    contador3 = 0

    for i in lista_trabajadores:
        if i['Sueldo'] < 800000:
            total_sueldos = total_sueldos + i['Sueldo']
            contador = contador +1
    print("Sueldos menores a 800.000: ", contador)
    print("Nombre                   Sueldo")
    for sueldo in lista_trabajadores:
        if sueldo['Sueldo'] < 800000:
            print(sueldo['Nombre'],"        ",sueldo['Sueldo'])
    print("")

    for j in lista_trabajadores:
        if j['Sueldo'] > 800000 and j['Sueldo'] < 2000000:
            total_sueldos = total_sueldos + j['Sueldo']
            contador2 = contador2 +1
    print("Sueldos entre 800.000 y 2.000.000: ", contador2)
    print("Nombre                  Sueldo")
    for sueldo1 in lista_trabajadores:
        if sueldo1['Sueldo'] > 800000 and sueldo1['Sueldo'] < 2000000:
            print(sueldo1['Nombre'],"        ",sueldo1['Sueldo'])
    print("")

    for k in lista_trabajadores:
        if k['Sueldo'] > 2000000:
            total_sueldos = total_sueldos + k['Sueldo']
            contador3 = contador3 +1
    print("Sueldos mayores a 2.000.000: ", contador3)
    print("Nombre                  Sueldo")
    for sueldo2 in lista_trabajadores:
        if sueldo2['Sueldo'] > 2000000:
            print(sueldo2['Nombre'],"        ",sueldo2['Sueldo'],)
    print("")
    print("Total sueldos: ", total_sueldos)


def ver_estadisticas(lista_trabajadores):
    total = 0
    lista_sueldos = []
    for i in lista_trabajadores:
        total = total + i['Sueldo']
        lista_sueldos.append(i['Sueldo'])
    sueldo_prom = total / 10
    sueldo_bajo = min(lista_sueldos)
    sueldo_alto = max(lista_sueldos)
    media_geometrica =est.geometric_mean(lista_sueldos)
    print("Sueldo mas bajo: ", sueldo_bajo)
    print("Sueldo mas alto: ", sueldo_alto)
    print("Sueldo promedio: ",sueldo_prom)
    print("Media geometrica: ", media_geometrica)

def reporte_sueldos(lista_trabajadores):

    informe = []

    for trabajador in lista_trabajadores:
        descuento_salud = trabajador['Sueldo'] * 0.07
        descuento_afp = trabajador['Sueldo'] * 0.12
        sueldo_liquido = trabajador['Sueldo'] - descuento_salud - descuento_afp
        informe.append({
            'Nombre' : trabajador['Nombre'],
            'Sueldo' : trabajador['Sueldo'],
            'Descuento salud' : descuento_salud,
            'Descuento afp' : descuento_afp,
            'Sueldo liquido' : sueldo_liquido
        })

    nombreArchivo = 'archivo.csv'

    encabezado = ['Nombre empleado','Sueldo Base','Descuento Salud','Descuento AFP','Sueldo Líquido']

    with open(nombreArchivo,'w') as archivo_csv:

        escritor = csv.DictWriter(archivo_csv,fieldnames=encabezado)

        escritor.writerow(encabezado)

        escritor.writerows(informe)
            
    print("Planilla generada con éxito")