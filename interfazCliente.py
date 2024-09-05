
#Variables de funcionalidad

nombre_clientes = ["clientes:"]

id_clientes = [len(nombre_clientes)]

deudaCobrar = ["clientes:"]

deudaPagar = ["clientes:"]

telefono = ["clientes:"]

#Menu: 
opciones = -1

while opciones != 5:
    print("\n1. -Ingresar clientes\n")
    print("2. -Editar cliente\n")
    print("3. -Eliminar cliente\n")
    print("4. -Mostrar cliente \n")
    print("5. -Cerrar sesion \n")
    opciones = int(input("Introduce la opcion: \n"))

    match opciones:
        case 1:
            print("\ningresar cliente")
            ingreso_nombre = input("\nIngresa el nombre del cliente: ")
            ingreso_telefono = input("\nIngrese el telefono del cliente: ")
            ingreso_deudaPagar = input("\nIngrese la deuda a pagar: ")
            ingreso_deudaCobrar = input("\nIngrese la deuda a cobrar: ")
            print("Cliente ingresado correctamente\n")

            nombre_clientes.append(ingreso_nombre)
            telefono.append(ingreso_telefono)
            deudaCobrar.append(ingreso_deudaCobrar)
            deudaPagar.append(ingreso_deudaPagar)
        case 2: 
            print("Que quieres editar: 1. Nombre, 2. Telefono, 3. Deuda a cobrar, 4. Deuda a pagar, 5.Cambiar todos los datos")
            eleccion_editar = int(input("Que quieres cambiar del usuario: "))
            if eleccion_editar == 1:
                print(nombre_clientes)
                eleccion_cliente = int(input("seleccionar cliente: \n"))
                nombre_clientes[eleccion_cliente] = input("Cambiar a: ")

            elif eleccion_editar == 2:
                print(nombre_clientes)
                eleccion_cliente = int(input("seleccionar cliente: \n"))
                telefono[eleccion_cliente] = input("Cambiar a: ")

            elif eleccion_editar == 3:
                print(nombre_clientes)
                eleccion_cliente = int(input("seleccionar cliente: \n"))
                deudaCobrar[eleccion_cliente] = input("Cambiar a: ")

            elif eleccion_editar == 4:
                print(nombre_clientes)
                eleccion_cliente = int(input("seleccionar cliente: \n"))
                deudaPagar[eleccion_cliente] = input("Cambiar a: ")

            elif eleccion_editar == 5:
                print(nombre_clientes)
                eleccion_cliente = int(input(" \n seleccionar cliente: "))
                print("\nCambiar nombre: ")
                nombre_clientes[eleccion_cliente] = input("Cambiar a: ")
                print("\nCambiar telefono: ")
                telefono[eleccion_cliente] = input("Cambiar a: ")
                print("\nCambiar deuda a pagar: ")
                deudaPagar[eleccion_cliente] = input("Cambiar a: ")
                print("\nCambiar deuda a cobrar: ")
                deudaCobrar[eleccion_cliente] = input("Cambiar a: ")

            else: 
                print("No existe esa opcion")

        case 3:
            print("Eliminar cliente: \n")
            print(nombre_clientes)
            eleccion_cliente = int(input(" \n seleccionar cliente: "))
            nombre_clientes.pop(eleccion_cliente)
            telefono.pop(eleccion_cliente)
            deudaCobrar.pop(eleccion_cliente)
            deudaPagar.pop(eleccion_cliente)

        case 4:
            print("\n",nombre_clientes,"\n")
            eleccion_cliente = int(input("seleccionar cliente: \n"))
            print(" - El nombre es: ", nombre_clientes[eleccion_cliente], "\n ", " -El telefono es ",telefono[eleccion_cliente], "\n", "- La deuda a cobrar es: ", deudaCobrar[eleccion_cliente], "\n","- La deuda a pagar es: ", deudaPagar[eleccion_cliente])
        case 5:
            print("Cerrando sesion")