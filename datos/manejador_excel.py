import openpyxl
import os

class ManejadorExcel:
    def __init__(self):
        self.archivo = "concesionaria.xlsx"
        self._inicializar_archivo()

    def _inicializar_archivo(self):
        # Crea el archivo con encabezados si no existe
        if not os.path.exists(self.archivo):
            wb = openpyxl.Workbook()
            hoja = wb.active
            hoja.title = "Ventas"
            hoja.append(["ID", "Cliente", "Teléfono", "Correo", "Marca", "Modelo", "Precio", "Fecha"])
            wb.save(self.archivo)

    def registrar_venta(self, datos):
        wb = openpyxl.load_workbook(self.archivo)
        hoja = wb.active
        # Calcula el ID sumando 1 a la cantidad de filas actuales
        nuevo_id = hoja.max_row
        fila = [nuevo_id] + datos
        hoja.append(fila)
        wb.save(self.archivo)

    def obtener_ventas(self):
        wb = openpyxl.load_workbook(self.archivo)
        hoja = wb.active
        ventas = []
        for fila in hoja.iter_rows(min_row=2, values_only=True):
            if fila[0] is not None:
                ventas.append(fila)
        return ventas

    def eliminar_venta(self, id_venta):
        wb = openpyxl.load_workbook(self.archivo)
        hoja = wb.active
        for row in range(2, hoja.max_row + 1):
            if hoja.cell(row=row, column=1).value == int(id_venta):
                hoja.delete_rows(row, 1)
                wb.save(self.archivo)
                return True
        return False
    