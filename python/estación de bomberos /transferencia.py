
saldo_emisor = 2000.0  # saldo de tu cuenta
saldo_receptor = 1500.0  # saldo receptor

while True:
    print("\nMenú:")
    print("1. Consultar saldo de las cuentas")
    print("2. Transferir dinero")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Tu saldo:", saldo_emisor)
        print("Saldo del receptor:", saldo_receptor)

    elif opcion == "2":
        monto = float(input("Cantidad a transferir: "))
        if monto > 1000:
            print("Fondo insuficiente (el monto máximo a transferir es $1000).")
        elif monto <= 0:
            print("Debe ingresar un monto válido.")
        elif saldo_emisor >= monto:
            saldo_emisor -= monto
            saldo_receptor += monto
            print("¡Transferencia exitosa!")
            print("Tu saldo:", saldo_emisor)
            print("Saldo del receptor:", saldo_receptor)
        else:
            print("Fondo insuficiente en tu cuenta.")

    elif opcion == "3":
        print("¡Programa finalizado!")
        break

    else:
        print("Opción no válida, intenta de nuevo.")
