import tkinter as tk  # Importar la biblioteca tkinter para crear la interfaz gráfica
from tkinter import messagebox, simpledialog  # Importar componentes específicos de tkinter
import sqlite3  # Importar la biblioteca sqlite3 para manejar la base de datos

# Clase que representa a un bombero
class Bombero:
    def __init__(self, id_bombero, nombre, apellido, rango):
        self.id_bombero = id_bombero  # ID del bombero
        self.nombre = nombre  # Nombre del bombero
        self.apellido = apellido  # Apellido del bombero
        self.rango = rango  # Rango del bombero (Sargento, Teniente, Comandante)

    def __str__(self):
        # Método para representar al bombero como una cadena
        return f"ID: {self.id_bombero}, Nombre: {self.nombre} {self.apellido}, Rango: {self.rango}"

# Clase que representa un vehículo
class Vehiculo:
    def __init__(self, id_vehiculo, tipo, cantidad):
        self.id_vehiculo = id_vehiculo  # ID del vehículo
        self.tipo = tipo  # Tipo de vehículo
        self.cantidad = cantidad  # Cantidad de vehículos de este tipo

    def __str__(self):
        # Método para representar el vehículo como una cadena
        return f"ID: {self.id_vehiculo}, Tipo: {self.tipo}, Cantidad: {self.cantidad}"

# Clase que representa la estación de bomberos
class EstacionBomberos:
    def __init__(self, id_estacion):
        self.id_estacion = id_estacion  # ID de la estación
        # Crear conexión a la base de datos SQLite
        self.conn = sqlite3.connect('estacion_bomberos.db')
        self.crear_tablas()  # Llamar al método para crear las tablas necesarias

    def crear_tablas(self):
        # Método para crear las tablas en la base de datos si no existen
        with self.conn:
            # Crear tabla para bomberos
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS bomberos (
                    id_bombero TEXT PRIMARY KEY,  # ID único del bombero
                    nombre TEXT,                   # Nombre del bombero
                    apellido TEXT,                 # Apellido del bombero
                    rango TEXT                     # Rango del bombero
                )
            ''')
            # Crear tabla para vehículos
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS vehiculos (
                    id_vehiculo TEXT PRIMARY KEY,  # ID único del vehículo
                    tipo TEXT,                     # Tipo de vehículo
                    cantidad INTEGER                # Cantidad de vehículos
                )
            ''')

    def agregar_bombero(self, id_bombero, nombre, apellido, rango):
        # Método para agregar un bombero a la base de datos
        try:
            with self.conn:
                # Insertar un nuevo bombero en la tabla
                self.conn.execute('INSERT INTO bomberos VALUES (?, ?, ?, ?)', 
                                  (id_bombero, nombre, apellido, rango))
            return True, "Bombero registrado correctamente."  # Retornar éxito
        except sqlite3.IntegrityError:
            return False, "El bombero ya está registrado."  # Manejar error de ID duplicado

    def agregar_vehiculo(self, id_vehiculo, tipo, cantidad):
        # Método para agregar un vehículo a la base de datos
        try:
            with self.conn:
                # Insertar un nuevo vehículo en la tabla
                self.conn.execute('INSERT INTO vehiculos VALUES (?, ?, ?)', 
                                  (id_vehiculo, tipo, cantidad))
            return True, "Vehículo registrado correctamente."  # Retornar éxito
        except sqlite3.IntegrityError:
            return False, "El vehículo ya está registrado."  # Manejar error de ID duplicado

    def editar_bombero(self, id_bombero, nombre=None, apellido=None, rango=None):
        # Método para editar los datos de un bombero
        with self.conn:
            # Actualizar el nombre si se proporciona
            if nombre:
                self.conn.execute('UPDATE bomberos SET nombre = ? WHERE id_bombero = ?', (nombre, id_bombero))
            # Actualizar el apellido si se proporciona
            if apellido:
                self.conn.execute('UPDATE bomberos SET apellido = ? WHERE id_bombero = ?', (apellido, id_bombero))
            # Actualizar el rango si se proporciona
            if rango:
                self.conn.execute('UPDATE bomberos SET rango = ? WHERE id_bombero = ?', (rango, id_bombero))
        return True, "Bombero actualizado correctamente."  # Retornar éxito

    def editar_vehiculo(self, id_vehiculo, tipo=None, cantidad=None):
        # Método para editar los datos de un vehículo
        with self.conn:
            # Actualizar el tipo si se proporciona
            if tipo:
                self.conn.execute('UPDATE vehiculos SET tipo = ? WHERE id_vehiculo = ?', (tipo, id_vehiculo))
            # Actualizar la cantidad si se proporciona
            if cantidad is not None:
                self.conn.execute('UPDATE vehiculos SET cantidad = ? WHERE id_vehiculo = ?', (cantidad, id_vehiculo))
        return True, "Vehículo actualizado correctamente."  # Retornar éxito

    def eliminar_bombero(self, id_bombero):
        # Método para eliminar un bombero de la base de datos
        with self.conn:
            self.conn.execute('DELETE FROM bomberos WHERE id_bombero = ?', (id_bombero,))
        return True, "Bombero eliminado."  # Retornar éxito

    def eliminar_vehiculo(self, id_vehiculo):
        # Método para eliminar un vehículo de la base de datos
        with self.conn:
            self.conn.execute('DELETE FROM vehiculos WHERE id_vehiculo = ?', (id_vehiculo,))
        return True, "Vehículo eliminado."  # Retornar éxito

    def obtener_bomberos(self):
        # Método para obtener todos los bomberos de la base de datos
        cursor = self.conn.execute('SELECT * FROM bomberos')  # Ejecutar consulta
        # Retornar lista de objetos Bombero
        return [Bombero(*row) for row in cursor]

    def obtener_vehiculos(self):
        # Método para obtener todos los vehículos de la base de datos
        cursor = self.conn.execute('SELECT * FROM vehiculos')  # Ejecutar consulta
        # Retornar lista de objetos Vehiculo
        return [Vehiculo(*row) for row in cursor]

# Clase que representa la aplicación principal
class App(tk.Tk):
    def __init__(self):
        super().__init__()  # Inicializar la clase base
        self.title("Estación de Bomberos - Básico")  # Título de la ventana
        self.geometry("500x400")  # Dimensiones de la ventana
        self.resizable(True, True)  # Permitir redimensionar la ventana

        self.estacion = EstacionBomberos("E001")  # Crear instancia de la estación de bomberos

        # Crear botones para cambiar vistas
        botones_frame = tk.Frame(self)  # Crear un marco para los botones
        botones_frame.pack(pady=5)  # Empaquetar el marco

        # Botones para las diferentes funcionalidades
        tk.Button(botones_frame, text="Registrar", command=self.mostrar_registrar).pack(side="left", padx=5)
        tk.Button(botones_frame, text="Mostrar", command=self.mostrar_mostrar).pack(side="left", padx=5)
        tk.Button(botones_frame, text="Editar", command=self.mostrar_editar).pack(side="left", padx=5)
        tk.Button(botones_frame, text="Eliminar", command=self.mostrar_eliminar).pack(side="left", padx=5)

        # Frames para cada sección de la aplicación
        self.frame_registrar = tk.Frame(self)  # Frame para registrar
        self.frame_mostrar = tk.Frame(self)  # Frame para mostrar
        self.frame_editar = tk.Frame(self)  # Frame para editar
        self.frame_eliminar = tk.Frame(self)  # Frame para eliminar

        # Crear los componentes de cada sección
        self.crear_registrar()
        self.crear_mostrar()
        self.crear_editar()
        self.crear_eliminar()

        self.mostrar_registrar()  # Mostrar vista inicial de registro

    def ocultar_frames(self):
        # Método para ocultar todos los frames
        self.frame_registrar.pack_forget()
        self.frame_mostrar.pack_forget()
        self.frame_editar.pack_forget()
        self.frame_eliminar.pack_forget()

    def mostrar_registrar(self):
        # Método para mostrar el frame de registro
        self.ocultar_frames()  # Ocultar otros frames
        self.frame_registrar.pack(fill="both", expand=True)  # Mostrar frame de registro

    def mostrar_mostrar(self):
        # Método para mostrar el frame de mostrar
        self.ocultar_frames()  # Ocultar otros frames
        self.actualizar_listas()  # Actualizar listas de bomberos y vehículos
        self.frame_mostrar.pack(fill="both", expand=True)  # Mostrar frame de mostrar

    def mostrar_editar(self):
        # Método para mostrar el frame de editar
        self.ocultar_frames()  # Ocultar otros frames
        self.frame_editar.pack(fill="both", expand=True)  # Mostrar frame de editar

    def mostrar_eliminar(self):
        # Método para mostrar el frame de eliminar
        self.ocultar_frames()  # Ocultar otros frames
        self.frame_eliminar.pack(fill="both", expand=True)  # Mostrar frame de eliminar

    def crear_registrar(self):
        # Método para crear los componentes del frame de registro
        f = self.frame_registrar  # Referencia al frame de registro

        tk.Label(f, text="Registrar Bombero").pack(pady=5)  # Etiqueta para registrar bombero

        # Entradas para los datos del bombero
        tk.Label(f, text="ID Bombero:").pack()
        self.id_bombero_entry = tk.Entry(f)  # Campo de entrada para ID del bombero
        self.id_bombero_entry.pack()

        tk.Label(f, text="Nombre:").pack()
        self.nombre_bombero_entry = tk.Entry(f)  # Campo de entrada para nombre del bombero
        self.nombre_bombero_entry.pack()

        tk.Label(f, text="Apellido:").pack()
        self.apellido_bombero_entry = tk.Entry(f)  # Campo de entrada para apellido del bombero
        self.apellido_bombero_entry.pack()

        tk.Label(f, text="Rango (Sargento, Teniente, Comandante):").pack()
        self.rango_bombero_entry = tk.Entry(f)  # Campo de entrada para rango del bombero
        self.rango_bombero_entry.pack()

        # Botón para registrar bombero
        tk.Button(f, text="Registrar Bombero", command=self.registrar_bombero).pack(pady=10)

        tk.Label(f, text="Registrar Vehículo").pack(pady=5)  # Etiqueta para registrar vehículo

        # Entradas para los datos del vehículo
        tk.Label(f, text="ID Vehículo:").pack()
        self.id_vehiculo_entry = tk.Entry(f)  # Campo de entrada para ID del vehículo
        self.id_vehiculo_entry.pack()

        tk.Label(f, text="Tipo:").pack()
        self.tipo_vehiculo_entry = tk.Entry(f)  # Campo de entrada para tipo del vehículo
        self.tipo_vehiculo_entry.pack()

        tk.Label(f, text="Cantidad:").pack()
        self.cantidad_vehiculo_entry = tk.Entry(f)  # Campo de entrada para cantidad del vehículo
        self.cantidad_vehiculo_entry.pack()

        # Botón para registrar vehículo
        tk.Button(f, text="Registrar Vehículo", command=self.registrar_vehiculo).pack(pady=10)

    def crear_mostrar(self):
        # Método para crear los componentes del frame de mostrar
        f = self.frame_mostrar  # Referencia al frame de mostrar

        tk.Label(f, text="Bomberos Registrados").pack()  # Etiqueta para bomberos registrados
        self.bomberos_listbox = tk.Listbox(f, width=60, height=10)  # Listbox para mostrar bomberos
        self.bomberos_listbox.pack(pady=5)

        tk.Label(f, text="Vehículos Registrados").pack()  # Etiqueta para vehículos registrados
        self.vehiculos_listbox = tk.Listbox(f, width=60, height=10)  # Listbox para mostrar vehículos
        self.vehiculos_listbox.pack(pady=5)

        # Botón para actualizar las listas
        tk.Button(f, text="Actualizar Listas", command=self.actualizar_listas).pack(pady=5)

    def crear_editar(self):
        # Método para crear los componentes del frame de editar
        f = self.frame_editar  # Referencia al frame de editar

        tk.Label(f, text="Editar Bombero").pack(pady=5)  # Etiqueta para editar bombero
        tk.Button(f, text="Editar Bombero", command=self.editar_bombero_dialog).pack(pady=5)  # Botón para editar bombero

        tk.Label(f, text="Editar Vehículo").pack(pady=5)  # Etiqueta para editar vehículo
        tk.Button(f, text="Editar Vehículo", command=self.editar_vehiculo_dialog).pack(pady=5)  # Botón para editar vehículo

    def crear_eliminar(self):
        # Método para crear los componentes del frame de eliminar
        f = self.frame_eliminar  # Referencia al frame de eliminar

        tk.Label(f, text="Eliminar Bombero").pack(pady=5)  # Etiqueta para eliminar bombero
        tk.Button(f, text="Eliminar Bombero", command=self.eliminar_bombero_dialog).pack(pady=5)  # Botón para eliminar bombero

        tk.Label(f, text="Eliminar Vehículo").pack(pady=5)  # Etiqueta para eliminar vehículo
        tk.Button(f, text="Eliminar Vehículo", command=self.eliminar_vehiculo_dialog).pack(pady=5)  # Botón para eliminar vehículo

    def registrar_bombero(self):
        # Método para registrar un bombero
        id_bombero = self.id_bombero_entry.get().strip()  # Obtener ID del bombero
        nombre = self.nombre_bombero_entry.get().strip()  # Obtener nombre del bombero
        apellido = self.apellido_bombero_entry.get().strip()  # Obtener apellido del bombero
        rango = self.rango_bombero_entry.get().strip()  # Obtener rango del bombero

        # Validaciones de entrada
        if not id_bombero:
            messagebox.showerror("Error", "Debe ingresar ID del bombero.")  # Error si no se ingresa ID
            return
        if not nombre.isalpha():
            messagebox.showerror("Error", "Nombre inválido. Solo letras permitidas.")  # Error si nombre no es válido
            return
        if not apellido.isalpha():
            messagebox.showerror("Error", "Apellido inválido. Solo letras permitidas.")  # Error si apellido no es válido
            return
        if rango not in ["Sargento", "Teniente", "Comandante"]:
            messagebox.showerror("Error", "Rango inválido. Debe ser Sargento, Teniente o Comandante.")  # Error si rango no es válido
            return

        # Intentar registrar el bombero
        success, msg = self.estacion.agregar_bombero(id_bombero, nombre, apellido, rango)
        if success:
            messagebox.showinfo("Éxito", msg)  # Mensaje de éxito
            # Limpiar los campos de entrada
            self.id_bombero_entry.delete(0, tk.END)
            self.nombre_bombero_entry.delete(0, tk.END)
            self.apellido_bombero_entry.delete(0, tk.END)
            self.rango_bombero_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", msg)  # Mensaje de error si no se pudo registrar

    def registrar_vehiculo(self):
        # Método para registrar un vehículo
        id_vehiculo = self.id_vehiculo_entry.get().strip()  # Obtener ID del vehículo
        tipo = self.tipo_vehiculo_entry.get().strip()  # Obtener tipo del vehículo
        cantidad = self.cantidad_vehiculo_entry.get().strip()  # Obtener cantidad del vehículo

        # Validaciones de entrada
        if not id_vehiculo:
            messagebox.showerror("Error", "Debe ingresar ID del vehículo.")  # Error si no se ingresa ID
            return
        if not tipo:
            messagebox.showerror("Error", "Debe ingresar tipo de vehículo.")  # Error si no se ingresa tipo
            return
        if not cantidad.isdigit():
            messagebox.showerror("Error", "Cantidad debe ser un número entero.")  # Error si cantidad no es un número
            return

        # Intentar registrar el vehículo
        success, msg = self.estacion.agregar_vehiculo(id_vehiculo, tipo, cantidad)
        if success:
            messagebox.showinfo("Éxito", msg)  # Mensaje de éxito
            # Limpiar los campos de entrada
            self.id_vehiculo_entry.delete(0, tk.END)
            self.tipo_vehiculo_entry.delete(0, tk.END)
            self.cantidad_vehiculo_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", msg)  # Mensaje de error si no se pudo registrar

    def actualizar_listas(self):
        # Método para actualizar las listas de bomberos y vehículos en la interfaz
        self.bomberos_listbox.delete(0, tk.END)  # Limpiar la lista de bomberos
        for b in self.estacion.obtener_bomberos():
            self.bomberos_listbox.insert(tk.END, str(b))  # Agregar cada bombero a la lista

        self.vehiculos_listbox.delete(0, tk.END)  # Limpiar la lista de vehículos
        for v in self.estacion.obtener_vehiculos():
            self.vehiculos_listbox.insert(tk.END, str(v))  # Agregar cada vehículo a la lista

    def editar_bombero_dialog(self):
        # Método para editar un bombero
        id_bombero = simpledialog.askstring("Editar Bombero", "Ingrese ID del bombero a editar:")  # Pedir ID del bombero
        if not id_bombero:
            return  # Salir si no se ingresa ID
        if id_bombero not in [b.id_bombero for b in self.estacion.obtener_bomberos()]:
            messagebox.showerror("Error", "No se encontró el bombero.")  # Error si no se encuentra el bombero
            return
        bombero = next(b for b in self.estacion.obtener_bomberos() if b.id_bombero == id_bombero)  # Obtener el bombero

        # Pedir nuevos datos para el bombero
        nombre = simpledialog.askstring("Editar Nombre", f"Nombre actual: {bombero.nombre}. Nuevo nombre (deje vacío para no cambiar):")
        apellido = simpledialog.askstring("Editar Apellido", f"Apellido actual: {bombero.apellido}. Nuevo apellido (deje vacío para no cambiar):")
        rango = simpledialog.askstring("Editar Rango", f"Rango actual: {bombero.rango}. Nuevo rango (Sargento, Teniente, Comandante, vacío para no cambiar):")

        # Validaciones de entrada
        if nombre and not nombre.isalpha():
            messagebox.showerror("Error", "Nombre inválido. Solo letras permitidas.")
            return
        if apellido and not apellido.isalpha():
            messagebox.showerror("Error", "Apellido inválido. Solo letras permitidas.")
            return
        if rango and rango not in ["Sargento", "Teniente", "Comandante"]:
            messagebox.showerror("Error", "Rango inválido.")
            return

        # Intentar editar el bombero
        success, msg = self.estacion.editar_bombero(id_bombero, nombre or None, apellido or None, rango or None)
        if success:
            messagebox.showinfo("Éxito", msg)  # Mensaje de éxito
            self.actualizar_listas()  # Actualizar listas
        else:
            messagebox.showerror("Error", msg)  # Mensaje de error si no se pudo editar

    def editar_vehiculo_dialog(self):
        # Método para editar un vehículo
        id_vehiculo = simpledialog.askstring("Editar Vehículo", "Ingrese ID del vehículo a editar:")  # Pedir ID del vehículo
        if not id_vehiculo:
            return  # Salir si no se ingresa ID
        if id_vehiculo not in [v.id_vehiculo for v in self.estacion.obtener_vehiculos()]:
            messagebox.showerror("Error", "No se encontró el vehículo.")  # Error si no se encuentra el vehículo
            return
        vehiculo = next(v for v in self.estacion.obtener_vehiculos() if v.id_vehiculo == id_vehiculo)  # Obtener el vehículo

        # Pedir nuevos datos para el vehículo
        tipo = simpledialog.askstring("Editar Tipo", f"Tipo actual: {vehiculo.tipo}. Nuevo tipo (deje vacío para no cambiar):")
        cantidad = simpledialog.askstring("Editar Cantidad", f"Cantidad actual: {vehiculo.cantidad}. Nueva cantidad (deje vacío para no cambiar):")

        # Validaciones de entrada
        if cantidad and not cantidad.isdigit():
            messagebox.showerror("Error", "Cantidad debe ser un número entero.")
            return

        # Intentar editar el vehículo
        success, msg = self.estacion.editar_vehiculo(id_vehiculo, tipo or None, cantidad or None)
        if success:
            messagebox.showinfo("Éxito", msg)  # Mensaje de éxito
            self.actualizar_listas()  # Actualizar listas
        else:
            messagebox.showerror("Error", msg)  # Mensaje de error si no se pudo editar

    def eliminar_bombero_dialog(self):
        # Método para eliminar un bombero
        id_bombero = simpledialog.askstring("Eliminar Bombero", "Ingrese ID del bombero a eliminar:")  # Pedir ID del bombero
        if not id_bombero:
            return  # Salir si no se ingresa ID
        success, msg = self.estacion.eliminar_bombero(id_bombero)  # Intentar eliminar el bombero
        if success:
            messagebox.showinfo("Éxito", msg)  # Mensaje de éxito
            self.actualizar_listas()  # Actualizar listas
        else:
            messagebox.showerror("Error", msg)  # Mensaje de error si no se pudo eliminar

    def eliminar_vehiculo_dialog(self):
        # Método para eliminar un vehículo
        id_vehiculo = simpledialog.askstring("Eliminar Vehículo", "Ingrese ID del vehículo a eliminar:")  # Pedir ID del vehículo
        if not id_vehiculo:
            return  # Salir si no se ingresa ID
        success, msg = self.estacion.eliminar_vehiculo(id_vehiculo)  # Intentar eliminar el vehículo
        if success:
            messagebox.showinfo("Éxito", msg)  # Mensaje de éxito
            self.actualizar_listas()  # Actualizar listas
        else:
            messagebox.showerror("Error", msg)  # Mensaje de error si no se pudo eliminar

# Punto de entrada de la aplicación
if __name__ == "__main__":
    app = App()  # Crear instancia de la aplicación
    app.mainloop()  # Iniciar el bucle principal de la interfaz gráfica
