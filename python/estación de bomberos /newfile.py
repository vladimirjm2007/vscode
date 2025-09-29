import tkinter as tk
from tkinter import messagebox, simpledialog

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
        return f"ID: {self.id_vehiculo}, Tipo: {self.tipo}, Cantidad: {self.cantidad}"

class EstacionBomberos:
    def __init__(self, id_estacion):
        self.id_estacion = id_estacion
        self.bomberos = {}
        self.vehiculos = {}

    def agregar_bombero(self, id_bombero, nombre, apellido, rango):
        if id_bombero in self.bomberos:
            return False, "El bombero ya está registrado."
        self.bomberos[id_bombero] = Bombero(id_bombero, nombre, apellido, rango)
        return True, "Bombero registrado correctamente."

    def agregar_vehiculo(self, id_vehiculo, tipo, cantidad):
        if id_vehiculo in self.vehiculos:
            return False, "El vehículo ya está registrado."
        self.vehiculos[id_vehiculo] = Vehiculo(id_vehiculo, tipo, cantidad)
        return True, "Vehículo registrado correctamente."

    def editar_bombero(self, id_bombero, nombre=None, apellido=None, rango=None):
        if id_bombero not in self.bomberos:
            return False, "No se encontró el bombero."
        bombero = self.bomberos[id_bombero]
        if nombre:
            bombero.nombre = nombre
        if apellido:
            bombero.apellido = apellido
        if rango:
            bombero.rango = rango
        return True, "Bombero actualizado correctamente."

    def editar_vehiculo(self, id_vehiculo, tipo=None, cantidad=None):
        if id_vehiculo not in self.vehiculos:
            return False, "No se encontró el vehículo."
        vehiculo = self.vehiculos[id_vehiculo]
        if tipo:
            vehiculo.tipo = tipo
        if cantidad:
            vehiculo.cantidad = cantidad
        return True, "Vehículo actualizado correctamente."

    def eliminar_bombero(self, id_bombero):
        if id_bombero in self.bomberos:
            del self.bomberos[id_bombero]
            return True, "Bombero eliminado."
        return False, "No se encontró el bombero."

    def eliminar_vehiculo(self, id_vehiculo):
        if id_vehiculo in self.vehiculos:
            del self.vehiculos[id_vehiculo]
            return True, "Vehículo eliminado."
        return False, "No se encontró el vehículo."

    def obtener_bomberos(self):
        return list(self.bomberos.values())

    def obtener_vehiculos(self):
        return list(self.vehiculos.values())

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Estación de Bomberos - Básico")
        self.geometry("500x400")
        self.resizable(True, True)

        self.estacion = EstacionBomberos("E001")

        # Crear botones para cambiar vistas
        botones_frame = tk.Frame(self)
        botones_frame.pack(pady=5)

        tk.Button(botones_frame, text="Registrar", command=self.mostrar_registrar).pack(side="left", padx=5)
        tk.Button(botones_frame, text="Mostrar", command=self.mostrar_mostrar).pack(side="left", padx=5)
        tk.Button(botones_frame, text="Editar", command=self.mostrar_editar).pack(side="left", padx=5)
        tk.Button(botones_frame, text="Eliminar", command=self.mostrar_eliminar).pack(side="left", padx=5)

        # Frames para cada sección
        self.frame_registrar = tk.Frame(self)
        self.frame_mostrar = tk.Frame(self)
        self.frame_editar = tk.Frame(self)
        self.frame_eliminar = tk.Frame(self)

        self.crear_registrar()
        self.crear_mostrar()
        self.crear_editar()
        self.crear_eliminar()

        self.mostrar_registrar()  # Mostrar vista inicial

    def ocultar_frames(self):
        self.frame_registrar.pack_forget()
        self.frame_mostrar.pack_forget()
        self.frame_editar.pack_forget()
        self.frame_eliminar.pack_forget()

    def mostrar_registrar(self):
        self.ocultar_frames()
        self.frame_registrar.pack(fill="both", expand=True)

    def mostrar_mostrar(self):
        self.ocultar_frames()
        self.actualizar_listas()
        self.frame_mostrar.pack(fill="both", expand=True)

    def mostrar_editar(self):
        self.ocultar_frames()
        self.frame_editar.pack(fill="both", expand=True)

    def mostrar_eliminar(self):
        self.ocultar_frames()
        self.frame_eliminar.pack(fill="both", expand=True)

    def crear_registrar(self):
        f = self.frame_registrar

        tk.Label(f, text="Registrar Bombero").pack(pady=5)

        tk.Label(f, text="ID Bombero:").pack()
        self.id_bombero_entry = tk.Entry(f)
        self.id_bombero_entry.pack()

        tk.Label(f, text="Nombre:").pack()
        self.nombre_bombero_entry = tk.Entry(f)
        self.nombre_bombero_entry.pack()

        tk.Label(f, text="Apellido:").pack()
        self.apellido_bombero_entry = tk.Entry(f)
        self.apellido_bombero_entry.pack()

        tk.Label(f, text="Rango (Sargento, Teniente, Comandante):").pack()
        self.rango_bombero_entry = tk.Entry(f)
        self.rango_bombero_entry.pack()

        tk.Button(f, text="Registrar Bombero", command=self.registrar_bombero).pack(pady=10)

        tk.Label(f, text="Registrar Vehículo").pack(pady=5)

        tk.Label(f, text="ID Vehículo:").pack()
        self.id_vehiculo_entry = tk.Entry(f)
        self.id_vehiculo_entry.pack()

        tk.Label(f, text="Tipo:").pack()
        self.tipo_vehiculo_entry = tk.Entry(f)
        self.tipo_vehiculo_entry.pack()

        tk.Label(f, text="Cantidad:").pack()
        self.cantidad_vehiculo_entry = tk.Entry(f)
        self.cantidad_vehiculo_entry.pack()

        tk.Button(f, text="Registrar Vehículo", command=self.registrar_vehiculo).pack(pady=10)

    def crear_mostrar(self):
        f = self.frame_mostrar

        tk.Label(f, text="Bomberos Registrados").pack()
        self.bomberos_listbox = tk.Listbox(f, width=60, height=10)
        self.bomberos_listbox.pack(pady=5)

        tk.Label(f, text="Vehículos Registrados").pack()
        self.vehiculos_listbox = tk.Listbox(f, width=60, height=10)
        self.vehiculos_listbox.pack(pady=5)

        tk.Button(f, text="Actualizar Listas", command=self.actualizar_listas).pack(pady=5)

    def crear_editar(self):
        f = self.frame_editar

        tk.Label(f, text="Editar Bombero").pack(pady=5)
        tk.Button(f, text="Editar Bombero", command=self.editar_bombero_dialog).pack(pady=5)

        tk.Label(f, text="Editar Vehículo").pack(pady=5)
        tk.Button(f, text="Editar Vehículo", command=self.editar_vehiculo_dialog).pack(pady=5)

    def crear_eliminar(self):
        f = self.frame_eliminar

        tk.Label(f, text="Eliminar Bombero").pack(pady=5)
        tk.Button(f, text="Eliminar Bombero", command=self.eliminar_bombero_dialog).pack(pady=5)

        tk.Label(f, text="Eliminar Vehículo").pack(pady=5)
        tk.Button(f, text="Eliminar Vehículo", command=self.eliminar_vehiculo_dialog).pack(pady=5)

    def registrar_bombero(self):
        id_bombero = self.id_bombero_entry.get().strip()
        nombre = self.nombre_bombero_entry.get().strip()
        apellido = self.apellido_bombero_entry.get().strip()
        rango = self.rango_bombero_entry.get().strip()

        if not id_bombero:
            messagebox.showerror("Error", "Debe ingresar ID del bombero.")
            return
        if not nombre.isalpha():
            messagebox.showerror("Error", "Nombre inválido. Solo letras permitidas.")
            return
        if not apellido.isalpha():
            messagebox.showerror("Error", "Apellido inválido. Solo letras permitidas.")
            return
        if rango not in ["Sargento", "Teniente", "Comandante"]:
            messagebox.showerror("Error", "Rango inválido. Debe ser Sargento, Teniente o Comandante.")
            return

        success, msg = self.estacion.agregar_bombero(id_bombero, nombre, apellido, rango)
        if success:
            messagebox.showinfo("Éxito", msg)
            self.id_bombero_entry.delete(0, tk.END)
            self.nombre_bombero_entry.delete(0, tk.END)
            self.apellido_bombero_entry.delete(0, tk.END)
            self.rango_bombero_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", msg)

    def registrar_vehiculo(self):
        id_vehiculo = self.id_vehiculo_entry.get().strip()
        tipo = self.tipo_vehiculo_entry.get().strip()
        cantidad = self.cantidad_vehiculo_entry.get().strip()

        if not id_vehiculo:
            messagebox.showerror("Error", "Debe ingresar ID del vehículo.")
            return
        if not tipo:
            messagebox.showerror("Error", "Debe ingresar tipo de vehículo.")
            return
        if not cantidad.isdigit():
            messagebox.showerror("Error", "Cantidad debe ser un número entero.")
            return

        success, msg = self.estacion.agregar_vehiculo(id_vehiculo, tipo, cantidad)
        if success:
            messagebox.showinfo("Éxito", msg)
            self.id_vehiculo_entry.delete(0, tk.END)
            self.tipo_vehiculo_entry.delete(0, tk.END)
            self.cantidad_vehiculo_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", msg)

    def actualizar_listas(self):
        self.bomberos_listbox.delete(0, tk.END)
        for b in self.estacion.obtener_bomberos():
            self.bomberos_listbox.insert(tk.END, str(b))

        self.vehiculos_listbox.delete(0, tk.END)
        for v in self.estacion.obtener_vehiculos():
            self.vehiculos_listbox.insert(tk.END, str(v))

    def editar_bombero_dialog(self):
        id_bombero = simpledialog.askstring("Editar Bombero", "Ingrese ID del bombero a editar:")
        if not id_bombero:
            return
        if id_bombero not in self.estacion.bomberos:
            messagebox.showerror("Error", "No se encontró el bombero.")
            return
        bombero = self.estacion.bomberos[id_bombero]

        nombre = simpledialog.askstring("Editar Nombre", f"Nombre actual: {bombero.nombre}. Nuevo nombre (deje vacío para no cambiar):")
        apellido = simpledialog.askstring("Editar Apellido", f"Apellido actual: {bombero.apellido}. Nuevo apellido (deje vacío para no cambiar):")
        rango = simpledialog.askstring("Editar Rango", f"Rango actual: {bombero.rango}. Nuevo rango (Sargento, Teniente, Comandante, vacío para no cambiar):")

        if nombre and not nombre.isalpha():
            messagebox.showerror("Error", "Nombre inválido. Solo letras permitidas.")
            return
        if apellido and not apellido.isalpha():
            messagebox.showerror("Error", "Apellido inválido. Solo letras permitidas.")
            return
        if rango and rango not in ["Sargento", "Teniente", "Comandante"]:
            messagebox.showerror("Error", "Rango inválido.")
            return

        success, msg = self.estacion.editar_bombero(id_bombero, nombre or None, apellido or None, rango or None)
        if success:
            messagebox.showinfo("Éxito", msg)
            self.actualizar_listas()
        else:
            messagebox.showerror("Error", msg)

    def editar_vehiculo_dialog(self):
        id_vehiculo = simpledialog.askstring("Editar Vehículo", "Ingrese ID del vehículo a editar:")
        if not id_vehiculo:
            return
        if id_vehiculo not in self.estacion.vehiculos:
            messagebox.showerror("Error", "No se encontró el vehículo.")
            return
        vehiculo = self.estacion.vehiculos[id_vehiculo]

        tipo = simpledialog.askstring("Editar Tipo", f"Tipo actual: {vehiculo.tipo}. Nuevo tipo (deje vacío para no cambiar):")
        cantidad = simpledialog.askstring("Editar Cantidad", f"Cantidad actual: {vehiculo.cantidad}. Nueva cantidad (deje vacío para no cambiar):")

        if cantidad and not cantidad.isdigit():
            messagebox.showerror("Error", "Cantidad debe ser un número entero.")
            return

        success, msg = self.estacion.editar_vehiculo(id_vehiculo, tipo or None, cantidad or None)
        if success:
            messagebox.showinfo("Éxito", msg)
            self.actualizar_listas()
        else:
            messagebox.showerror("Error", msg)

    def eliminar_bombero_dialog(self):
        id_bombero = simpledialog.askstring("Eliminar Bombero", "Ingrese ID del bombero a eliminar:")
        if not id_bombero:
            return
        success, msg = self.estacion.eliminar_bombero(id_bombero)
        if success:
            messagebox.showinfo("Éxito", msg)
            self.actualizar_listas()
        else:
            messagebox.showerror("Error", msg)

    def eliminar_vehiculo_dialog(self):
        id_vehiculo = simpledialog.askstring("Eliminar Vehículo", "Ingrese ID del vehículo a eliminar:")
        if not id_vehiculo:
            return
        success, msg = self.estacion.eliminar_vehiculo(id_vehiculo)
        if success:
            messagebox.showinfo("Éxito", msg)
            self.actualizar_listas()
        else:
            messagebox.showerror("Error", msg)

if __name__ == "__main__":
    app = App()
    app.mainloop()
