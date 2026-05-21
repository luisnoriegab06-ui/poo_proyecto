import os
from openpyxl import Workbook, load_workbook

class ManejadorExcel:
    def __init__(self):
        self.archivo = "concesionaria.xlsx"
        self.inicializar_excel()

    def inicializar_excel(self):
        """Crea el archivo y los encabezados si no existe"""
        if not os.path.exists(self.archivo):
            wb = Workbook()
            ws = wb.active
            ws.append(["Cliente", "Teléfono", "Correo", "Marca", "Modelo", "Precio", "Fecha"])
            wb.save(self.archivo)
            wb.close()

    def registrar_venta(self, datos_lista):
        """Registra la fila y hace el guardado inmediato (Punto Excel)"""
        self.inicializar_excel()
        wb = load_workbook(self.archivo)
        ws = wb.active
        ws.append(datos_lista)
        wb.save(self.archivo)
        wb.close()

    def obtener_ventas(self):
        """Lee los datos para mostrarlos en la tabla"""
        self.inicializar_excel()
        wb = load_workbook(self.archivo)
        ws = wb.active
        datos = []
        for row in ws.iter_rows(min_row=2, values_only=True):
            if row[0]: # Si la celda no está vacía
                datos.append(row)
        wb.close()
        return datos

    def eliminar_venta(self, id_venta):
        """Método listo para no romper el controlador si lo usas"""
        # (Aquí iría tu lógica de borrado por ID si tienes la tabla configurada)
        return True