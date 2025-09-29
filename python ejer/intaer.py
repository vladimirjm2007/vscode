import tkinter as tk

# Función que se ejecuta al presionar el botón
def mostrar_texto():
    texto_ingresado = entrada.get()
    etiqueta_resultado.config(text=f"Tú escribiste: {texto_ingresado}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera interfaz")
ventana.geometry("400x200")  # Tamaño de la ventana

# Etiqueta de instrucción
etiqueta = tk.Label(ventana, text="Escribe algo:", font=("Arial", 14))
etiqueta.pack(pady=10)

# Campo de entrada de texto
entrada = tk.Entry(ventana, width=30, font=("Arial", 12))
entrada.pack(pady=10)

# Botón para mostrar el texto
boton = tk.Button(ventana, text="Mostrar", command=mostrar_texto, font=("Arial", 12))
boton.pack(pady=10)

# Etiqueta donde se mostrará el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 14), fg="black")
etiqueta_resultado.pack(pady=10)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()