def mayoredad(edad):

    if edad >= 18:
        return True
    else:
        return False

def main():
    # El usuario ingresa su edad
    edad = int(input("Por favor, ingresa tu edad: "))

    # Determinar si es mayor o menor de edad utilizando la función
    if mayoredad(edad):
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

if __name__ == "__main__":
    main()