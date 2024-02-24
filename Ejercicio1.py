'''
Crear una calculadora que realice operaciones basica como suma, resta, multiplicacion y division.
Utiliza funciones para cada operacion y permite al usuario elegir la operacion deseada.
'''

#definimos las funciones
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "¡Error!, No se puede dividir por cero."

def calculadora():
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    opcion = input("Seleccione la operación que desea realizar: ")

    if opcion == '1':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("El resultado de la suma es:", suma(num1, num2))
    elif opcion == '2':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("El resultado de la resta es:", resta(num1, num2))
    elif opcion == '3':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("El resultado de la multiplicación es:", multiplicacion(num1, num2))
    elif opcion == '4':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("El resultado de la división es:", division(num1, num2))
    else:
        print("Opción no válida")

#Mandamos a llamar la funcion de calculadora
calculadora()