import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from controlador.concesionaria import ControladorConcesionaria

class AppConcesionaria:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión - Concesionaria")
        self.root.geometry("950x550")
        
        self.controlador = ControladorConcesionaria()
        
        self.crear_interfaz()
        self.cargar_datos()

    def crear_interfaz(self):
        marco_form = tk.LabelFrame(self.root, text="Registrar Nueva Venta", padx=10, pady=10)
        marco_form.pack(fill="x", padx=10, pady=10)

        tk.Label(marco_form, text="Nombre Cliente:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_cliente = tk.Entry(marco_form)
        self.entry_cliente.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(marco_form, text="Teléfono:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_telefono = tk.Entry(marco_form)
        self.entry_telefono.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(marco_form, text="Correo:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_correo = tk.Entry(marco_form)
        self.entry_correo.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(marco_form, text="Marca Auto:").grid(row=1, column=2, padx=5, pady=5)
        # Uso de Combobox (Punto 14)
        self.combo_marca = ttk.Combobox(marco_form, values=["Toyota", "Honda", "Ford", "Nissan", "Chevrolet"], state="readonly")
        self.combo_marca.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(marco_form, text="Modelo:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_modelo = tk.Entry(marco_form)
        self.entry_modelo.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(marco_form, text="Precio:").grid(row=2, column=2, padx=5, pady=5)
        self.entry_precio = tk.Entry(marco_form)
        self.entry_precio.grid(row=2, column=3, padx=5, pady=5)

        tk.Label(marco_form, text="Fecha:").grid(row=3, column=0, padx=5, pady=5)
        # Uso de DateEntry (Punto 14)
        self.entry_fecha = DateEntry(marco_form, width=17, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.entry_fecha.grid(row=3, column=1, padx=5, pady=5)

        marco_botones = tk.Frame(self.root)
        marco_botones.pack(pady=5)

        tk.Button(marco_botones, text="Registrar Venta", command=self.registrar).grid(row=0, column=0, padx=10)
        tk.Button(marco_botones, text="Limpiar Campos", command=self.limpiar).grid(row=0, column=1, padx=10)
        tk.Button(marco_botones, text="Eliminar Seleccionado", command=self.eliminar).grid(row=0, column=2, padx=10)

        # Tabla Treeview
        self.tree = ttk.Treeview(self.root, columns=("ID", "Cliente", "Tel", "Correo", "Marca", "Modelo", "Precio", "Fecha"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=110)
        self.tree.column("ID", width=30)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def registrar(self):
        cliente = self.entry_cliente.get().strip()
        tel = self.entry_telefono.get().strip()
        correo = self.entry_correo.get().strip()
        marca = self.combo_marca.get()
        modelo = self.entry_modelo.get().strip()
        precio_str = self.entry_precio.get().strip()
        fecha = self.entry_fecha.get()

        # Validaciones (Vacíos)
        if not all([cliente, tel, correo, marca, modelo, precio_str, fecha]):
            messagebox.showwarning("Atención", "No se permiten campos vacíos.")
            return

        # Validaciones (Formatos y Rangos)
        try:
            precio = float(precio_str)
            if precio <= 0: raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número válido mayor a 0.")
            return

        self.controlador.procesar_registro(cliente, tel, correo, marca, modelo, precio, fecha)
        messagebox.showinfo("Éxito", "La venta ha sido registrada en el Excel.")
        self.limpiar()
        self.cargar_datos()

    def limpiar(self):
        self.entry_cliente.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.combo_marca.set('')
        self.entry_modelo.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)

    def cargar_datos(self):
        # Limpia la tabla antes de recargar
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Obtiene e inserta datos desde Excel
        for fila in self.controlador.obtener_registros():
            self.tree.insert("", tk.END, values=fila)

    def eliminar(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Por favor seleccione un registro de la tabla.")
            return
        
        if messagebox.askyesno("Confirmación", "¿Está seguro de eliminar esta venta?"):
            item = self.tree.item(seleccion)
            id_venta = item['values'][0]
            self.controlador.eliminar_registro(id_venta)
            self.cargar_datos()
            messagebox.showinfo("Eliminado", "Registro borrado correctamente.")
            