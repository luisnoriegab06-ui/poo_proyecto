class Venta:
    def __init__(self, auto, cliente, fecha):
        self.__auto = auto
        self.__cliente = cliente
        self.__fecha = fecha

    @property
    def auto(self): return self.__auto
    @property
    def cliente(self): return self.__cliente
    @property
    def fecha(self): return self.__fecha

    def mostrar_datos(self):
        return f"Venta registrada el {self.fecha} a nombre de {self.cliente.nombre}"
    