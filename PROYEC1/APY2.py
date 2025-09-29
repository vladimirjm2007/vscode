# Definir las variables globales para evitar errores de referencia
cantidad_producto1 = 0
cantidad_producto2 = 0
cantidad_producto3 = 0
cantidad_producto4 = 0
cantidad_producto5 = 0

# Definir variables globales para CPU, RAM y discos
def cantidad_cpu():
    return 0

def cantidad_ram():
    return 0

def cantidad_disco():
    return 0

def producto1():
    producto1 = "mause"
    return producto1

def producto2():
    producto2 = "teclado"
    return producto2

def producto3():
    producto3 = "monitor"
    return producto3

def producto4():
    producto4 = "CPU", "ram", "disco duro"
    return producto4

def producto5():
    producto5 = "impresora"
    return producto5

def mostrar_cantidad():
    try:
        return f"Cantidad de {producto1()}: {cantidad_producto1}, Cantidad de {producto2()}: {cantidad_producto2}, cantidad de {producto3()}: {cantidad_producto3}, cantidad de {producto4()}: {cantidad_producto4}, cantidad de {producto5()}: {cantidad_producto5}"
    except Exception:
        return "No hay productos registrados."

def main():
    global cantidad_producto1, cantidad_producto2, cantidad_producto3, cantidad_producto4, cantidad_producto5  # Declarar las variables como globales para modificarlas
    while True:
        print("|--------------------------------|")
        print("|bienvenido, que desea registrar.|")
        print("|--------------------------------|")
        print("|opciones:                       |")
        print("|1: mause                        |")
        print("|2: teclado                      |")
        print("|3: monitor                      |")
        print("|4: cpu, ram, disco duro         |")
        print("|5: impresora                    |")
        print("|6: mostrar productos registrados|")
        print("|--------------------------------|")
        registro_producto = input("ingrese una opcion (1, 2, 3, 4, 5, 6) o '7' para terminar: ")
        if registro_producto == "1":
            cantidad_producto1 = int(input("ingrese la cantidad del producto 1: "))
            print("Producto 1 registrado:", producto1())
        elif registro_producto == "2":
            cantidad_producto2 = int(input("ingrese la cantidad del producto 2: "))
            print("Producto 2 registrado:", producto2())
        elif registro_producto == "3":
            print("Productos registrados:", mostrar_cantidad())
        elif registro_producto == "4":
            producto3 = int(input("que produactu desea registrar 1 cpu, 2 ram, 3 disco duro: "))
            if producto3 == "1":
                print("cuantas CPU desdea registrar:")
                cant_cpu=int(input("imgrese:"))
            elif producto3 =="2":
                print("cuantas menoria ram vas a registrar?")
                cant_ram=int(input("ingrese:"))
            elif producto3=="3":
                print("cuantos discos duros vas a registar?")
                cant_discos=int(input("ingrese:"))
            print("Producto 3 registrado: monitor")
        elif registro_producto == "5":
            cantidad_producto4 = int(input("ingrese la cantidad del producto 4: "))
            print("Producto 4 registrado: impresora")
        elif registro_producto == "6":
            cantidad_producto5 = int(input("ingrese la cantidad del producto 5: "))
            print("Producto 5 registrado: laptop")
        elif registro_producto == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()