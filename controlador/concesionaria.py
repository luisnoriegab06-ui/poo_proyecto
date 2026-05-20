from modelo.cliente import Cliente
from modelo.auto import Auto
from modelo.venta import Venta
from datos.manejador_excel import ManejadorExcel

class ControladorConcesionaria:
    def __init__(self):
        self.bd = ManejadorExcel()

    def procesar_registro(self, nombre, telefono, correo, marca, modelo, precio, fecha):
        # Crear objetos
        cliente = Cliente(nombre, telefono, correo)
        auto = Auto(marca, modelo, float(precio))
        venta = Venta(auto, cliente, fecha)
        
        # Demostración de Polimorfismo
        entidades = [cliente, auto, venta]
        for entidad in entidades:
            print(entidad.mostrar_datos()) # Llama la versión correcta de cada clase

        # Guardar en Excel
        datos = [cliente.nombre, cliente.telefono, cliente.correo, 
                 auto.marca, auto.modelo, auto.precio, venta.fecha]
        self.bd.registrar_venta(datos)

    def obtener_registros(self):
        return self.bd.obtener_ventas()

    def eliminar_registro(self, id_venta):
        return self.bd.eliminar_venta(id_venta)
    