class Auto:
    def __init__(self, marca, modelo, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.precio = precio 

    @property
    def marca(self): return self.__marca
    
    @property
    def modelo(self): return self.__modelo
    
    @property
    def precio(self): return self.__precio

    @precio.setter
    def precio(self, valor):
        valor_numerico = float(valor)
        if valor_numerico <= 0:
            raise ValueError("El precio del vehículo no puede ser negativo o cero.")
        self.__precio = valor_numerico

    def mostrar_datos(self):
        return f"Auto: {self.marca} {self.modelo} | Precio: ${self.precio}"