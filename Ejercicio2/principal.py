import clases as c
import os 

agendas = c.Agendas()

def agendarContacto():
    try:
        os.system("cls || clear")
        nombre = input("Nombre: ")
        numerotelf = int(input("Numero de telefono: "))
        contacto = c.Contacto(nombre, numerotelf)
        agendas.agregar_contacto(contacto)
    except:
        print("Intenta nuevamente")

def menu():
    while True:
        os.system("cls || clear")
        print("Tienes: " , str(len(agendas.contactos)))
        print("1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Salir")
        try:
            opcion = int(input("Opción: "))
            if opcion == 1:
                agendarContacto()
            elif opcion == 2:
                print("ver contactos")
                agendas.mostrar_contactos()
                os.system("pause")
            elif opcion == 3:
                break
            else:
                print("Opción no válida")
        except:
            print("Error: Ingrese un número entero")

def main():
    menu()

if __name__ == "__main__":
    main()