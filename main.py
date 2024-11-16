def mostrar_menu():
    print("\n****************************************")
    print("****************************************")
    print("*****                              *****")
    print("***** Menú del Sistema de Reservas *****")
    print("*****                              *****")
    print("****************************************")
    print("****************************************\n")
    print(" 1. Crear una nueva sala de cine ")
    print("99. Salir ")
    print("\n****************************************")
def main():


    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            print("Crear una nueva sala de cine")
        elif opcion == "99":
            print("Saliendo del Sistema. ¡¡¡¡ ** Hasta pronto ** !!!!")
            break
        else:
            print("La opción seleccionada no es correcta. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()