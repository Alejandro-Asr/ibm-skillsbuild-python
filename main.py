from sala_cine import SalaCine
import utils

def mostrar_menu():
    print("\n****************************************")
    print("****************************************")
    print("*****                              *****")
    print("***** Menú del Sistema de Reservas *****")
    print("*****                              *****")
    print("****************************************")
    print("****************************************\n")
    print(" 1. Crear una nueva sala de cine")
    print(" 2. Agregar Asiento")
    print(" 3. Reservar un asiento")
    print(" 4. Cancelar una reserva")
    print(" 5. Mostrar todos los asientos")
    print("99. Salir ")
    print("\n****************************************")

def mostrar_mensajes(codigo: int, mensaje: str = ""):
     # Diccionario para manejar los mensajes según el código
    mensajes_por_codigo = {
        1: "No existe sala. Por favor para continuar debe crear una sala",
        2: "Ya existe una sala creada",
        97: "Error: {mensaje}",
        98: "La opción seleccionada no es correcta. Por favor, intenta de nuevo.",
        99: "Saliendo del Sistema. ¡¡¡¡ ** Hasta pronto ** !!!!"
    }

    # Asignar mensaje predeterminado si no se proporciona
    if not mensaje:
        mensaje = mensajes_por_codigo.get(codigo, "Código no reconocido. Por favor contacte con el Administrador.")
        
    print(mensaje)
    input("Presiona Enter para continuar...")

def main():
    sala = None  # Inicialmente no hay sala creada

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            print("Creando una nueva sala de cine")
            if sala is not None:
                mostrar_mensajes(2)
                continue
            try:
                precio_base = float(input("Ingresa el precio base para la sala: "))
                sala = SalaCine(precio_base)
                print("La sala de cine fue creada con exito")
            except ValueError as e:
                if("could not convert string to float" in str(e)):
                    mostrar_mensajes(3, "Valor no admitido")
                else:
                    mostrar_mensajes(3, e)

        elif opcion == "2":
            if sala is None:
                mostrar_mensajes(1)
                continue
            
            try:
                fila = input("Ingresa la fila del asiento (por ejemplo, A): ")
                numero = int(input("Ingresa el número del asiento: "))
                sala.agregar_asiento(numero, fila)
                mostrar_mensajes(None, f"Asiento {fila}{numero} agregado exitosamente.")
            except ValueError as e:
                if("invalid literal for int() with base 10" in str(e)):
                    mostrar_mensajes(3, "Valor no admitido")
                else:
                    mostrar_mensajes(3, e)

        elif opcion == "3":
            if sala is None:
                mostrar_mensajes(1)
                continue
            try:
                fila = input("Ingresa la fila del asiento (por ejemplo, A): ")
                numero = int(input("Ingresa el número del asiento: "))
                edad = int(input("Ingresa la edad del espectador: "))
                dia = input("Ingresa el día (por ejemplo, miércoles): ")
                sala.reservar_asiento(numero, fila, edad, dia)
                print(f"Asiento {fila}{numero} reservado exitosamente.")
            except ValueError as e:
                mostrar_mensajes(3, e)

        elif opcion == "4":
            if sala is None:
                mostrar_mensajes(1)
                continue
            fila = input("Ingresa la fila del asiento (por ejemplo, A): ")
            numero = int(input("Ingresa el número del asiento: "))
            try:
                sala.cancelar_reserva(numero, fila)
                print(f"Reserva del asiento {fila}{numero} cancelada exitosamente.")
            except ValueError as e:
                mostrar_mensajes(3, e)

        elif opcion == "5":
            if sala is None:
                print("No existe sala crear, Por favor cree una sala")
            print("\n*** Estado de asientos *****************")
            for asiento in sala.mostrar_asientos():
                print(asiento)
                input("Presiona Enter para continuar...")

        elif opcion == "99":
            mostrar_mensajes(99)
            break

        else:
            mostrar_mensajes(98)

if __name__ == "__main__":
    main()