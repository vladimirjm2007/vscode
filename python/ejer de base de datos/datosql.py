import sqlite3

# Crear la conexión a la base de datos
def crear_conexion():
    conn = sqlite3.connect("bomberos.db")
    return conn

# Crear la tabla de bomberos si no existe
def crear_tabla(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bomberos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            bombero_id TEXT UNIQUE NOT NULL,
            rango TEXT NOT NULL
        )
    """)
    conn.commit()

# Agregar un bombero a la base de datos
def agregar_bombero(conn, nombre, apellido, bombero_id, rango):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO bomberos (nombre, apellido, bombero_id, rango)
            VALUES (?, ?, ?, ?)
        """, (nombre, apellido, bombero_id, rango))
        conn.commit()
        print("Bombero agregado correctamente.")
    except sqlite3.IntegrityError:
        print("Error: El ID del bombero ya existe.")

# Mostrar todos los bomberos en la base de datos
def mostrar_bomberos(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bomberos")
    bomberos = cursor.fetchall()
    if bomberos:
        print("\nLista de bomberos:")
        for bombero in bomberos:
            print(f"ID: {bombero[0]}, Nombre: {bombero[1]}, Apellido: {bombero[2]}, ID Bombero: {bombero[3]}, Rango: {bombero[4]}")
    else:
        print("No hay bomberos registrados.")

# Actualizar la información de un bombero
def actualizar_bombero(conn, bombero_id, nombre=None, apellido=None, rango=None):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bomberos WHERE bombero_id = ?", (bombero_id,))
    bombero = cursor.fetchone()
    if bombero:
        updates = []
        params = []
        if nombre:
            updates.append("nombre = ?")
            params.append(nombre)
        if apellido:
            updates.append("apellido = ?")
            params.append(apellido)
        if rango:
            updates.append("rango = ?")
            params.append(rango)
        params.append(bombero_id)
        update_query = f"UPDATE bomberos SET {', '.join(updates)} WHERE bombero_id = ?"
        cursor.execute(update_query, params)
        conn.commit()
        print("Bombero actualizado correctamente.")
    else:
        print("Error: No se encontró ningún bombero con ese ID.")

# Eliminar un bombero de la base de datos
def eliminar_bombero(conn, bombero_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bomberos WHERE bombero_id = ?", (bombero_id,))
    if cursor.rowcount > 0:
        conn.commit()
        print("Bombero eliminado correctamente.")
    else:
        print("Error: No se encontró ningún bombero con ese ID.")

# Menú principal
def menu():
    conn = crear_conexion()
    crear_tabla(conn)

    while True:
        print("\n--- Menú de Gestión de Bomberos ---")
        print("1. Agregar bombero")
        print("2. Mostrar bomberos")
        print("3. Actualizar bombero")
        print("4. Eliminar bombero")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del bombero: ")
            apellido = input("Ingrese el apellido del bombero: ")
            bombero_id = input("Ingrese el ID del bombero: ")
            rango = input("Ingrese el rango del bombero: ")
            agregar_bombero(conn, nombre, apellido, bombero_id, rango)

        elif opcion == "2":
            mostrar_bomberos(conn)

        elif opcion == "3":
            bombero_id = input("Ingrese el ID del bombero a actualizar: ")
            nombre = input("Nuevo nombre (deje en blanco para no cambiar): ")
            apellido = input("Nuevo apellido (deje en blanco para no cambiar): ")
            rango = input("Nuevo rango (deje en blanco para no cambiar): ")
            actualizar_bombero(conn, bombero_id, nombre or None, apellido or None, rango or None)

        elif opcion == "4":
            bombero_id = input("Ingrese el ID del bombero a eliminar: ")
            eliminar_bombero(conn, bombero_id)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

    conn.close()

# Ejecutar el programa
if __name__ == "__main__":
    menu()