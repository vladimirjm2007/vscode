# Simulación de procesamiento de empleados desde un archivo CSV simulado
datos_csv = """id,nombre,departamento,salario
1,Juan,IT,3000
2,María,Ventas,2800
3,Rodrigo,IT,4000"""

filas = datos_csv.strip().split('\n')
encabezados = filas[0].split(',')
empleados = []

for fila in filas[1:]:
    valores = fila.split(',')
    empleado = {
        "id": valores[0],
        "nombre": valores[1],
        "departamento": valores[2],
        "salario": float(valores[3])
    }
    empleados.append(empleado)

# Mostrar empleados del departamento IT
for emp in empleados:
    if emp["departamento"] == "IT":
        print(f"Empleado IT: {empleado}")