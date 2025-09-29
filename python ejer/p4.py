# Sistema de generación de informe de empleados productivos
empleados = [
    {"nombre": "Alicia", "tareas_completadas": 12},
    {"nombre": "Bruno", "tareas_completadas": 5},
    {"nombre": "Camila", "tareas_completadas": 15},
    {"nombre": "Daniel", "tareas_completadas": 3}
]

# Eliminar empleados con menos de 6 tareas completadas
for emp in empleados:
    if emp["tareas_completadas"] < 6:
        empleados.remove(emp)

# Generar informe
print("Informe de productividad:")
for emp in empleados:
    print(f"- {emp['nombre']}: {emp['tareas_completadas']} tareas")