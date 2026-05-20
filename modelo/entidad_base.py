from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, telefono, correo):
        # Atributos privados (Encapsulamiento)
        self.__nombre = nombre
        self.__telefono = telefono
        self.__correo = correo

    # Getters y Setters
    @property
    def nombre(self): return self.__nombre
    @nombre.setter
    def nombre(self, valor): self.__nombre = valor

    @property
    def telefono(self): return self.__telefono
    @telefono.setter
    def telefono(self, valor): self.__telefono = valor

    @property
    def correo(self): return self.__correo
    @correo.setter
    def correo(self, valor): self.__correo = valor

    # Clase Abstracta
    @abstractmethod
    def mostrar_datos(self):
        pass
    