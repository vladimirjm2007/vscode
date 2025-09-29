class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto.mostrar_info())


class CantidadProducto:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def mostrar_cantidad(self):
        return f"Producto: {self.producto.nombre}, Cantidad: {self.cantidad}"


class RegistroCantidad:
    def __init__(self):
        self.cantidades = []

    def agregar_cantidad(self, cantidad_producto):
        self.cantidades.append(cantidad_producto)

    def mostrar_todas_cantidades(self):
        for cantidad in self.cantidades:
            print(cantidad.mostrar_cantidad())


class RegistrarProducto:
    def __init__(self):
        self.inventario = Inventario()

    def registrar(self, nombre, precio):
        nuevo_producto = Producto(nombre, precio)
        self.inventario.agregar_producto(nuevo_producto)
        print(f"Producto {nombre} registrado con éxito.")

