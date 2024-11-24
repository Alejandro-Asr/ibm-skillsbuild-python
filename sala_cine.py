from asiento import Asiento

class SalaCine:
    def __init__(self, precio_base: float):
        self.__asientos = []
        self.__precio_base = precio_base

    # Método privado para validar filas
    def __validar_fila(self, fila: str):
        if not fila:
            raise ValueError("El dato fila es obligatorio.")
        if not fila.isalpha() or len(fila) > 1 or fila != fila.upper():
            raise ValueError("Solo se puede introducir una letra mayúscula para indicar la fila.")

    def __validar_dia_semana(self, dia: str):
        dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        dia = dia.strip().lower()
        return dia in dias_semana

    # Agregar un asiento
    def agregar_asiento(self, numero: int, fila: str):
        # Validar fila
        self.__validar_fila(fila)

        if any(asiento.get_numero() == numero and asiento.get_fila() == fila for asiento in self.__asientos):
            raise ValueError("El asiento ya está registrado.")
        self.__asientos.append(Asiento(numero, fila, self.__precio_base))

    # Reservar asiento
    def reservar_asiento(self, numero: int, fila: str, edad: int, dia: str):
        # Validar fila y día de la semana
        self.__validar_fila(fila)
        

        if(not self.__validar_dia_semana(dia)):
            raise ValueError("El día de la semana no es correcto.\n Los valores permitidos son lunes, martes, miércoles, jueves, viernes, sábado, domingo")
        
        asiento = self.buscar_asiento(numero, fila)
        if asiento.is_reservado():
            raise ValueError("El asiento ya está reservado.")

        # Calcular precio con descuentos
        precio = self.__precio_base
        if dia.lower() == "miércoles":
            precio *= 0.8  # 20% descuento por día del espectador
        if edad >= 65:
            precio *= 0.7  # 30% descuento para mayores de 65 años

        asiento.set_precio(precio)
        asiento.set_reservado(True)

    # Cancelar reserva
    def cancelar_reserva(self, numero: int, fila: str):
        # Validar fila
        self.__validar_fila(fila)

        asiento = self.buscar_asiento(numero, fila)
        if not asiento.is_reservado():
            raise ValueError("El asiento no está reservado.")
        asiento.set_reservado(False)
        asiento.set_precio(self.__precio_base)  # Restaurar precio base

    # Mostrar asientos
    def mostrar_asientos(self):
        return [str(asiento) for asiento in self.__asientos]

    # Buscar asiento
    def buscar_asiento(self, numero: int, fila: str):
        # Validar fila
        self.__validar_fila(fila)
        
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                return asiento
        raise ValueError("Asiento no encontrado.")
        
