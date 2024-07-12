import funciones as fn

lista_trabajadores = [] 


while True:
    print("\nBienvenidos a analisis de sueldos")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir de programa\n")

    try:
        opcion = int(input("Seleccione la opcion deseada: \n"))

        if opcion == 1:
            fn.asignar_sueldos_aleatorios(lista_trabajadores)
        
        elif opcion == 2:
            fn.clasificar_sueldos(lista_trabajadores)
        
        elif opcion == 3:
            fn.ver_estadisticas(lista_trabajadores)

        elif opcion == 4:
            fn.reporte_sueldos(lista_trabajadores)
        
        elif opcion == 5:
            print("Finalizando programa...")
            print("Desarrollado por Bastian Castro")
            print("Rut 19.338.439-0")
            break

        else:
            print("Seleccione una opción válida")
    except:
        print("Opcion invalida, intente nuevamente")
