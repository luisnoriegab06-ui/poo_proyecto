from modelo.entidad_base import Persona

class Cliente(Persona):
    def __init__(self, nombre, telefono, correo):
        # Herencia con super()
        super().__init__(nombre, telefono, correo)

    # Polimorfismo
    def mostrar_datos(self):
        return f"Cliente: {self.nombre} | Contacto: {self.correo}"
    