biografia = {
    'nombre5': 'Esther',
    'apellidos': 'Vallejos Yarhui',
    'edad': 20,
    'fecha de nacimiento': '14/02/2002',
    'mascotas': {
        'perro': {'nombre': 'Susana con S', 'edad': 2}
    },
    'familia': {
        'padres': {'nombreM': 'Eusebia', 'nombreP': 'Rosendo', 'edadM': 53, 'edadP': 50},
        'hermanos': {'nombre4': 'Cristian', 'nombre6': 'Tomas', 'edad4': 23, 'edad6': 17 },
        'hermanas': {'nombre1': 'Adelin', 'nombre2': 'Remedios', 'nombre3': 'Maria Elena', 'edad1': 28, 'edad2': 26, 'edad3': 2}
    }
}
while True:
    print("----------------------------------")
    print("debe seleccionar las siguientes opciones")
    print("1.-imprimir todo mis datos")
    print("2.-salir")
    opcion = input("ingrese la opcion: ")
    if opcion == "1":
         print (biografia)
    elif opcion == "2":
        break
    else:
        print("opcion incorrecta")
