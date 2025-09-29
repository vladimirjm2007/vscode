# Sistema para calcular pago por horas trabajadas
registros = [
    {"empleado": "Sofía", "horas": 8},
    {"empleado": "Diego", "horas": 7.5},
    {"empleado": "Elena", "horas": 9}
]

tarifa_por_hora = 20

total_pagado = 0
for reg in registros:
    horas = reg["horas"]  # ❌ No se convierte a float
    pago = horas * tarifa_por_hora
    total_pagado += pago
    print(f"{reg['empleado']}: ${pago}")

print(f"Total a pagar: ${total_pagado}")