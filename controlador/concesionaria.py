from datetime import datetime
from tkinter import messagebox
from modelo.cliente import Cliente
from modelo.auto import Auto
from modelo.venta import Venta
from datos.manejador_excel import ManejadorExcel

class ControladorConcesionaria:
    def __init__(self, vista=None):
        self.bd = ManejadorExcel()
        self.vista = vista # Guarda la referencia de la vista si es necesaria

    def procesar_registro(self, nombre, telefono, correo, marca, modelo, precio, fecha):
        # 1. VALIDACIÓN DE FECHA INCORRECTA (Ajuste pedido por la maestra)
        try:
            # Intenta convertir el texto a una fecha real. Soporta formatos con "/" o "-"
            if "/" in fecha:
                fecha_validada = datetime.strptime(fecha, "%d/%m/%Y")
            elif "-" in fecha:
                fecha_validada = datetime.strptime(fecha, "%d-%m-%Y")
            else:
                # Si no tiene un formato claro, intenta el estándar común
                fecha_validada = datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            # Si la fecha no existe (ej: 31/02/2026 o texto), manda error y detiene el proceso
            messagebox.showerror("Error de Seguridad", "La fecha ingresada no es válida o no existe en el calendario.")
            return False

        # 2. VALIDACIÓN DE LÓGICA DE AUTO Y PRECIO
        try:
            # Validar que los campos de texto obligatorios no estén vacíos
            if not nombre.strip() or not marca.strip() or not modelo.strip():
                raise ValueError("Los campos de texto no pueden estar vacíos o contener solo espacios.")
            
            # Intenta convertir el precio a número flotante
            precio_numerico = float(precio)
            if precio_numerico <= 0:
                raise ValueError("El precio del vehículo debe ser un número estrictamente mayor a cero.")

        except ValueError as e:
            # Atrapa si el usuario escribió letras en el precio o dejó campos vacíos
            messagebox.showerror("Error de Lógica en Auto", f"Datos del vehículo incorrectos: {e}")
            return False

        # 3. CREACIÓN DE OBJETOS SEGURA (Si pasa las validaciones de arriba)
        try:
            cliente = Cliente(nombre, telefono, correo)
            auto = Auto(marca, modelo, precio_numerico)
            venta = Venta(auto, cliente, fecha)
            
            # Demostración de Polimorfismo (Se mantiene intacto para tu rúbrica)
            entidades = [cliente, auto, venta]
            for entidad in entidades:
                print(entidad.mostrar_datos()) # Llama la versión correcta de cada clase

            # Guardar en Excel (Punto Excel - Persistencia segura)
            datos = [cliente.nombre, cliente.telefono, cliente.correo, 
                     auto.marca, auto.modelo, auto.precio, venta.fecha]
            
            self.bd.registrar_venta(datos)
            messagebox.showinfo("Éxito", "Registro guardado correctamente en la base de datos de Excel.")
            return True

        except Exception as e:
            messagebox.showerror("Error del Sistema", f"No se pudo completar el registro: {e}")
            return False

    def obtener_registros(self):
        return self.bd.obtener_ventas()

    def eliminar_registro(self, id_venta):
        try:
            resultado = self.bd.eliminar_venta(id_venta)
            messagebox.showinfo("Éxito", "Registro eliminado correctamente del archivo Excel.")
            return resultado
        except Exception as e:
            messagebox.showerror("Error al eliminar", f"No se pudo borrar el registro: {e}")
            return False
    