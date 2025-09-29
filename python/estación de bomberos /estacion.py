class Bombero:
    def __init__(self, id_bombero, nombre, apellido, rango):
        self.id_bombero = id_bombero
        self.nombre = nombre
        self.apellido = apellido
        self.rango = rango

    def __str__(self):
        return f"ID: {self.id_bombero}, Nombre: {self.nombre} {self.apellido}, Rango: {self.rango}"


class Vehiculo:
    def __init__(self, id_vehiculo, tipo, cantidad):
        self.id_vehiculo = id_vehiculo
        self.tipo = tipo
        self.cantidad = cantidad

    def __str__(self):
        return f"ID: {self.id_vehiculo}, Tipo: {self.tipo}, cantidad:{self.cantidad}"


class EstacionBomberos:
    def __init__(self, id_estacion):
        self.id_estacion = id_estacion
        self.bomberos = {}
        self.vehiculos = {}

    def registrar_bombero(self):
        id_bombero = input("Ingrese ID del bombero: ").strip()
        if id_bombero in self.bomberos:
            print("El bombero ya está registrado.")
            return

        while True:
            nombre = input("Ingrese nombre del bombero: ").strip()
            if nombre.replace(" ", "").isalpha():
                break
            else:
                print("Nombre inválido. Solo se permiten letras.")

        while True:
            apellido = input("Ingrese apellido del bombero: ").strip()
            if apellido.replace(" ", "").isalpha():
                break
            else:
                print("Apellido inválido. Solo se permiten letras.")
        
        # Corrección de la indentación y lógica para seleccionar el rango
        while True:
            print("Seleccione el rango:")
            print("1. Sargento")
            print("2. Teniente")
            print("3. Comandante")
            opcion_rango = input("Establezca el rango (1-3): ").strip()
            
            rango = "" # Inicializar rango
            if opcion_rango == "1":
                rango = "Sargento"
                break
            elif opcion_rango == "2":
                rango = "Teniente"
                break
            elif opcion_rango == "3":
                rango = "Comandante"
                break
            else:
                print("Opción de rango no válida. Por favor, intente de nuevo.")
               
        self.bomberos[id_bombero] = Bombero(id_bombero, nombre, apellido, rango)
        print("Bombero registrado correctamente.")

    def registrar_vehiculo(self):
        id_vehiculo = input("Ingrese ID del vehículo: ").strip()
        if id_vehiculo in self.vehiculos:
            print("El vehículo ya está registrado.")
            return
        tipo = input("Ingrese tipo de vehículo: ").strip()
        cantidad = input("ingrese la cantidad: ").strip()
        self.vehiculos[id_vehiculo] = Vehiculo(id_vehiculo, tipo, cantidad)
        print("Vehículo registrado correctamente.")

    def mostrar_bomberos(self):
        if not self.bomberos:
            print("No hay bomberos registrados.")
        else:
            print("Bomberos registrados:")
            for bombero in self.bomberos.values():
                print(bombero)

    def mostrar_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos registrados.")
        else:
            print("Vehículos registrados:")
            for vehiculo in self.vehiculos.values():
                print(vehiculo)

    def editar_bombero(self):
        id_bombero = input("Ingrese ID del bombero a editar: ").strip()
        if id_bombero not in self.bomberos:
            print("No se encontró el bombero.")
            return

        bombero = self.bomberos[id_bombero]

        nombre_nuevo = input(f"Ingrese nuevo nombre (actual: {bombero.nombre}, deje vacío para no cambiar): ").strip()
        apellido_nuevo = input(f"Ingrese nuevo apellido (actual: {bombero.apellido}, deje vacío para no cambiar): ").strip()

        # Edición del rango
        while True:
            print(f"Rango actual: {bombero.rango}")
            print("Seleccione el nuevo rango (deje vacío para no cambiar):")
            print("1. Sargento")
            print("2. Teniente")
            print("3. Comandante")
            opcion_rango_nueva = input("Establezca el rango (1-3): ").strip()

            if not opcion_rango_nueva: # Si el usuario no ingresa nada, no se cambia el rango
                break

            rango_nuevo = ""
            if opcion_rango_nueva == "1":
                rango_nuevo = "Sargento"
                break
            elif opcion_rango_nueva == "2":
                rango_nuevo = "Teniente"
                break
            elif opcion_rango_nueva == "3":
                rango_nuevo = "Comandante"
                break
            else:
                print("Opción de rango no válida. Por favor, intente de nuevo.")

        if nombre_nuevo:
            if nombre_nuevo.replace(" ", "").isalpha():
                bombero.nombre = nombre_nuevo
            else:
                print("Nombre inválido. Solo se permiten letras. El nombre no fue cambiado.")

        if apellido_nuevo:
            if apellido_nuevo.replace(" ", "").isalpha():
                bombero.apellido = apellido_nuevo
            else:
                print("Apellido inválido. Solo se permiten letras. El apellido no fue cambiado.")
        
        if rango_nuevo: # Solo actualiza si se seleccionó un nuevo rango
            bombero.rango = rango_nuevo

        print("Bombero actualizado correctamente.")

    def editar_vehiculo(self):
        id_vehiculo = input("Ingrese ID del vehículo a editar: ").strip()
        if id_vehiculo not in self.vehiculos:
            print("No se encontró el vehículo.")
            return
        
        vehiculo = self.vehiculos[id_vehiculo]
        tipo_nuevo = input(f"Ingrese nuevo tipo (actual: {vehiculo.tipo}, deje vacío para no cambiar): ").strip()
        cantidad_nueva = input(f"ingrese la nueva cantidad (actual: {vehiculo.cantidad}, deje vacio para no cambiar): ").strip()
        
        if tipo_nuevo:
            vehiculo.tipo = tipo_nuevo
        elif cantidad_nueva:
            vehiculo.cantidad = cantidad_nueva
            print("Vehículo actualizado correctamente.")
        else:
            print("No se realizó ningún cambio en el tipo de vehículo.")


    def eliminar_bombero(self):
        id_bombero = input("Ingrese ID del bombero a eliminar: ").strip()
        if id_bombero in self.bomberos:
            del self.bomberos[id_bombero]
            print("Bombero eliminado.")
        else:
            print("No se encontró el bombero.")

    def eliminar_vehiculo(self):
        id_vehiculo = input("Ingrese ID del vehículo a eliminar: ").strip()
        if id_vehiculo in self.vehiculos:
            del self.vehiculos[id_vehiculo]
            print("Vehículo eliminado.")
        else:
            print("No se encontró el vehículo.")


def menu():
    print("\n--- Menú Estación de Bomberos ---")
    print("1. Registrar bombero")
    print("2. Registrar vehículo")
    print("3. Mostrar bomberos")
    print("4. Mostrar vehículos")
    print("5. Editar bombero")
    print("6. Editar vehículo")
    print("7. Eliminar bombero")
    print("8. Eliminar vehículo")
    print("9. Salir")
    print("La ID de esta estacion es :I012")


def main():
    estacion = EstacionBomberos(id_estacion="E001")
    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            estacion.registrar_bombero()
        elif opcion == "2":
            estacion.registrar_vehiculo()
        elif opcion == "3":
            estacion.mostrar_bomberos()
        elif opcion == "4":
            estacion.mostrar_vehiculos()
        elif opcion == "5":
            estacion.editar_bombero()
        elif opcion == "6":
            estacion.editar_vehiculo()
        elif opcion == "7":
            estacion.eliminar_bombero()
        elif opcion == "8":
            estacion.eliminar_vehiculo()
        elif opcion == "9":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()