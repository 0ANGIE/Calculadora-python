def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ValueError("No se puede dividir entre cero")
    if x < 0 or y < 0:
        raise ValueError("No se puede divir con numeros negativos")
    return x / y

print("Seleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

while True:
    opcion = input("Ingrese el numero de acuerdo con la operacin que dese a realizar: ")

    if opcion in ("1", "2", "3", "4"):
        break
    else:
        print("Esa no es una opcion valida")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if opcion == "1":
    resultado = suma(num1, num2)
elif opcion == "2":
    resultado = resta(num1, num2)
elif opcion == "3":
    try:
        resultado = multiplicacion(num1, num2)
    except ValueError as e:
        print(e)
        exit()
elif opcion == "4":
    try:
        resultado = division(num1, num2)
    except ValueError as e:
        print(e)
        exit()

print("El resultado es de la operacion es:", resultado)