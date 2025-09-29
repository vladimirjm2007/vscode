import tkinter as tk

raiz = tk.Tk()
raiz.title("interfaz_prac")
raiz.geometry("400x300")

#texto en pantalla
eti = tk.Label(raiz, text="Hola, usuario!", font=("Arial", 14))
eti.pack(pady=10)

#boton que recaciona a esta definicion muestra el texto en la terminal
def saludar():
    print("hola como estas usuario")
boton = tk.Button(raiz, text="saludar", command=saludar)
boton.pack(pady=5)


#entrada de texto
entrada = tk.Entry(raiz, width=30)
entrada.pack(pady=5)
#muesetra el texto en la terminal
def mosrar_texto():
    texto = entrada.get()
    print("ingresaste: ", texto)
tk.Button(raiz, text="mostrar", command=mosrar_texto).pack()

#permite multiples lineas de texto
area = tk.Text(raiz, height=5, width=40)
area.pack(pady=5)

area.insert(tk.END, "texto inicial")
contenido = area.get("1.0", tk.END)#optiene todo el texto




raiz.mainloop()
