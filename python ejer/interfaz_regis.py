import tkinter as tk
raiz = tk.Tk()
raiz.title("Registro de Empleados")
raiz.geometry("400x300")
raiz.configure(bg="#f0f0f0")

# Etiquetas y campos de entrada
etiqueta_nombre = tk.Label(raiz, text="Nombre:")
etiqueta_nombre.pack(pady=5)

entrada_nombre = tk.Entry(raiz, width=30, font=("Arial", 12))
entrada_nombre.pack(pady=5)

etiqueta_apellido = tk.Label(raiz, text="Apellido:")
etiqueta_apellido.pack(pady=5)

entrada_apellido = tk.Entry(raiz, width=30, font=("Arial", 12))
entrada_apellido.pack(pady=5)

etiqueta_id = tk.Label(raiz, text="ID Empleado:")
etiqueta_id.pack(pady=5)

entrada_id = tk.Entry(raiz, width=30, font=("Arial", 12))
entrada_id.pack(pady=5) 

etiqueta_departamento = tk.Label(raiz, text="Departamento:")
etiqueta_departamento.pack(pady=5)

entrada_departamento = tk.Entry(raiz, width=30, font=("Arial", 12))
entrada_departamento.pack(pady=5)   

etiqueta_resultado = tk.Label(raiz, text="", bg="#f0f0f0", font=("Arial", 12))
etiqueta_resultado.pack(pady=10)  

def registrar_empleado():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    emp_id = entrada_id.get()
    departamento = entrada_departamento.get()
    if nombre and apellido and emp_id and departamento:
        etiqueta_resultado.config(text=f"Empleado {nombre} {apellido} registrado exitosamente.", fg="green")
        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)
        entrada_id.delete(0, tk.END)
        entrada_departamento.delete(0, tk.END)
    else:
        etiqueta_resultado.config(text="Por favor, complete todos los campos.", fg="red")


boton_registrar = tk.Button(raiz, text="Registrar", command=registrar_empleado, font=("Arial", 12), bg="#4CAF50", fg="white")
boton_registrar.pack(pady=10)

raiz.mainloop()