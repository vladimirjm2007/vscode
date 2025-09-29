def calculadora(operacion, num1, num2):
            if operacion == "1":
                return num1 + num2
            elif operacion == "2":
                return num1 - num2
            elif operacion == "3":
                return num1 * num2
            elif operacion == "4":
                        if num2 != 0:
                            return num1 / num2
                        else:
                            return "Error: Division by zero"
            else:
                return "Error: Operacion no valida"

def calcular(operacion, num1, num2):
    return calculadora(operacion, num1, num2)
def main():
        print("Calculadora Simple")
        operacion = input("Ingrese la operacion (1 suma, 2 resta, 3 multiplicacion, 4 division 5 para salir): ")
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = calcular(operacion, num1, num2)
        print(f"El resultado de la {operacion} es: {resultado}")
        
              
if __name__ == "__main__":
    main()