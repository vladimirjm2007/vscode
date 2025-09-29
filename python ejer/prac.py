""""
la= input("introduce: ")
cantidad = sum(1 for c in la if c.isalpha())
print(f"su texto tiene {cantidad} letras.")
"""
###CALCULADORA DE VENTA###
#al final debe mostrar el total de ventas (nombre, cantidad, precio ) #
"""""
def registrar_producto(nombre, cantidad, precio):

    nombre = input("ingrese el nombre del producto: ")
    try:
        cantidad = input("ingrese la cantidad: ")
        precio = int(input("ingrese el precio del producto: "))
        print("producto agregado exitosamente.")
        producto = (nombre, cantidad, precio)
        
    except ValueError:
       print("producto invalido. ")
    
def mostar_producto(producto):

    if not producto:
     print("no hay productos regisatrados.")
     return
    print("productos registrados:")
    for i, u,  in enumerate(producto, 1):
       print(f"{i}.nombre:{u['nombre']}")
       print(f"{i}. cantidad:{u['cantidad']}")
       print(f"{i}precio:{u['precio']}")

def main():
   productos =[]
   while True:
      print("1. Registrar producto.")
      print("2. Mostar productos")
      print("3. Salir")
      opcion = input("eliga una opcion: ")

      if opcion == "1":
       registrar_producto
      elif opcion == "2":
        mostar_producto
      elif opcion =="3":
         print("saliendo del programa.")
         break  
    
if __name__ =="__main__":
    main()
"""""
# Simulación de cálculo de nómina con bonos por desempeño
empleados = [
    {"nombre": "Ana", "salario": 3000, "desempeno": 4.5},
    {"nombre": "Luis", "salario": 2500, "desempeno": 3.8},
    {"nombre": "Carlos", "salario": 3200, "desempeno": 4.9},
]

bono_alto = 500
bono_medio = 200

print("Nómina con bonos:")
for emp in empleados:
    if emp["desempeno"] >= 4.0:
        bono = bono_medio
    elif emp["desempeno"] >= 4.8:
        bono = bono_alto
    else:
        bono = 0
    total = emp["salario"] + bono
    print(f"{emp['nombre']}: ${total} (bono: ${bono})")