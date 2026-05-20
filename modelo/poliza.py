from abc import ABC, abstractmethod


# Clase abstracta: el molde de todas las pólizas
class Poliza(ABC):
    def __init__(self, titular, edad, prima_base, fecha):
        self.titular = titular           # nombre del asegurado
        self.edad = edad                 # edad del asegurado
        self.prima_base = prima_base     # monto anual base
        self.fecha = fecha               # fecha de inicio

    # Método abstracto: cada tipo de póliza calcula la prima distinto
    @abstractmethod
    def calcular_prima_mensual(self):
        pass

    # Representación en texto de la póliza
    def __str__(self):
        tipo = self.__class__.__name__
        return f"{tipo} | {self.titular} | Prima mensual: ${self.calcular_prima_mensual():,.2f}"


# Póliza de Auto: prima base dividida entre 12
class PolizaAuto(Poliza):
    def calcular_prima_mensual(self):
        return round(self.prima_base / 12, 2)


# Póliza de Vida: prima base/12 + ajuste si la edad es mayor a 40
class PolizaVida(Poliza):
    def calcular_prima_mensual(self):
        prima = self.prima_base / 12
        if self.edad > 40:
            prima *= 1 + ((self.edad - 40) * 0.01)
        return round(prima, 2)


# Póliza de Salud: prima base dividida entre 12
class PolizaSalud(Poliza):
    def calcular_prima_mensual(self):
        return round(self.prima_base / 12, 2)


# Diccionario que conecta el nombre del tipo con su clase
TIPOS_POLIZA = {
    "Auto": PolizaAuto,
    "Vida": PolizaVida,
    "Salud": PolizaSalud,
}