# Diccionario para almacenar la información de los clientes
clientes = {}

# Función para ingresar un nuevo cliente
def ingresar_cliente():
    nombre = input("\nIngresa el nombre del cliente: ")
    telefono = input("\nIngresa el teléfono del cliente: ")
    deuda_pagar = input("\nIngresa la deuda a pagar: ")
    deuda_cobrar = input("\nIngresa la deuda a cobrar: ")
    
    clientes[nombre] = {
        "telefono": telefono,
        "deuda_pagar": deuda_pagar,
        "deuda_cobrar": deuda_cobrar
    }
    print("Cliente ingresado correctamente\n")
    print(clientes)

# Función para editar un cliente
def editar_cliente():
    nombre = input("\nIngresa el nombre del cliente que deseas editar: ")
    if nombre in clientes:
        print("1. Nombre")
        print("2. Teléfono")
        print("3. Deuda a cobrar")
        print("4. Deuda a pagar")
        print("5. Cambiar todos los datos")
        eleccion_editar = input("\n¿Qué quieres cambiar del cliente? ")

        if eleccion_editar == "1":
            nuevo_nombre = input("Ingresa el nuevo nombre: ")
            clientes[nuevo_nombre] = clientes.pop(nombre)
        elif eleccion_editar == "2":
            clientes[nombre]["telefono"] = input("Ingresa el nuevo teléfono: ")
        elif eleccion_editar == "3":
            clientes[nombre]["deuda_cobrar"] = input("Ingresa la nueva deuda a cobrar: ")
        elif eleccion_editar == "4":
            clientes[nombre]["deuda_pagar"] = input("Ingresa la nueva deuda a pagar: ")
        elif eleccion_editar == "5":
            nuevo_nombre = input("Ingresa el nuevo nombre: ")
            telefono = input("Ingresa el nuevo teléfono: ")
            deuda_cobrar = input("Ingresa la nueva deuda a cobrar: ")
            deuda_pagar = input("Ingresa la nueva deuda a pagar: ")
            clientes.pop(nombre)
            clientes[nuevo_nombre] = {
                "telefono": telefono,
                "deuda_cobrar": deuda_cobrar,
                "deuda_pagar": deuda_pagar
            }
        else:
            print("Opción no válida.")
    else:
        print("Cliente no encontrado.")

# Función para eliminar un cliente
def eliminar_cliente():
    nombre = input("\nIngresa el nombre del cliente que deseas eliminar: ")
    if nombre in clientes:
        del clientes[nombre]
        print("Cliente eliminado correctamente.\n")
    else:
        print("Cliente no encontrado.")

# Función para mostrar un cliente
def mostrar_cliente():
    nombre = input("\nIngresa el nombre del cliente que deseas mostrar: ")
    if nombre in clientes:
        cliente = clientes[nombre]
        print(f"\nNombre: {nombre}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Deuda a cobrar: {cliente['deuda_cobrar']}")
        print(f"Deuda a pagar: {cliente['deuda_pagar']}")
    else:
        print("Cliente no encontrado.")

# Menú principal
opcion = -1

while opcion != 5:
    print("\n1. Ingresar cliente")
    print("2. Editar cliente")
    print("3. Eliminar cliente")
    print("4. Mostrar cliente")
    print("5. Cerrar sesión")
    opcion = input("Introduce la opción: ")

    if opcion == "1":
        ingresar_cliente()
    elif opcion == "2":
        editar_cliente()
    elif opcion == "3":
        eliminar_cliente()
    elif opcion == "4":
        mostrar_cliente()
    elif opcion == "5":
        print("Cerrando sesión.")
        exit()
    else:
        print("Opción no válida.")
