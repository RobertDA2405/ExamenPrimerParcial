def otorgar_beca(nota):
    if nota > 95:
        return True
    else:
        return False

def main():
    nota_estudiante = float(input("Ingrese la nota del estudiante (en porcentaje): "))

    if otorgar_beca(nota_estudiante):
        print("¡Felicidades! El estudiante califica para recibir una beca.")
    else:
        print("El estudiante no califica para recibir una beca.")

if __name__ == "__main__":
    main()