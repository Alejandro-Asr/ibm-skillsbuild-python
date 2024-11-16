class Asiento:
    def __init__(self, numero: int, fila: str, precio_base: float):
        self.__numero = numero
        self.__fila = fila
        self.__reservado = False
        self.__precio = precio_base

    # Getters and setters
    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def is_reservado(self):
        return self.__reservado

    def get_precio(self):
        return self.__precio

    def set_reservado(self, estado: bool):
        self.__reservado = estado

    def set_precio(self, precio: float):
        self.__precio = precio

    def __str__(self):
        estado = "Reservado" if self.__reservado else "Disponible"
        return f"Asiento {self.__fila}{self.__numero}: {estado}, Precio: ${self.__precio:.2f}"
