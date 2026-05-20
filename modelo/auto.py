class Auto:
    def __init__(self, marca, modelo, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio

    @property
    def marca(self): return self.__marca
    @property
    def modelo(self): return self.__modelo
    @property
    def precio(self): return self.__precio

    # Polimorfismo
    def mostrar_datos(self):
        return f"Auto: {self.marca} {self.modelo} | Precio: ${self.precio}"