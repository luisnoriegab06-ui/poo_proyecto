import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import DateEntry

# Importamos DESDE nuestras carpetas
from modelo.poliza import TIPOS_POLIZA
from datos.manejador_excel import ManejadorExcel


class VentanaPolizas(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.title("Sistema de Pólizas · UAG")
        self.geometry("600x520")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Creamos el manejador de Excel (controlador)
        self.excel = ManejadorExcel()

        # Lista en memoria para las pólizas de esta sesión
        self.polizas = []

        # Construimos el formulario
        self.crear_formulario()

    def crear_formulario(self):
        # Título de la ventana
        ctk.CTkLabel(self, text="Registro de Pólizas de Seguro",
                     font=("Arial", 22, "bold")).pack(pady=(20, 5))

        # Frame que agrupa todos los campos
        self.frame_form = ctk.CTkFrame(self)
        self.frame_form.pack(padx=30, pady=15, fill="x")

        # Fila 0: Titular
        ctk.CTkLabel(self.frame_form, text="Titular:", font=("Arial", 14)).grid(
            row=0, column=0, padx=20, pady=10, sticky="w")
        self.entry_titular = ctk.CTkEntry(
            self.frame_form, width=300, placeholder_text="Nombre completo")
        self.entry_titular.grid(row=0, column=1, padx=20, pady=10)

        # Fila 1: Edad
        ctk.CTkLabel(self.frame_form, text="Edad:", font=("Arial", 14)).grid(
            row=1, column=0, padx=20, pady=10, sticky="w")
        self.entry_edad = ctk.CTkEntry(
            self.frame_form, width=300, placeholder_text="Ej: 35")
        self.entry_edad.grid(row=1, column=1, padx=20, pady=10)

        # Fila 2: Tipo de póliza (lista desplegable)
        ctk.CTkLabel(self.frame_form, text="Tipo:", font=("Arial", 14)).grid(
            row=2, column=0, padx=20, pady=10, sticky="w")
        self.combo_tipo = ctk.CTkComboBox(
            self.frame_form, width=300,
            values=["Auto", "Vida", "Salud"], state="readonly")
        self.combo_tipo.grid(row=2, column=1, padx=20, pady=10)
        self.combo_tipo.set("Auto")

        # Fila 3: Prima base anual
        ctk.CTkLabel(self.frame_form, text="Prima anual ($):", font=("Arial", 14)).grid(
            row=3, column=0, padx=20, pady=10, sticky="w")
        self.entry_prima = ctk.CTkEntry(
            self.frame_form, width=300, placeholder_text="Ej: 12000")
        self.entry_prima.grid(row=3, column=1, padx=20, pady=10)

        # Fila 4: Fecha de inicio (selector de calendario)
        ctk.CTkLabel(self.frame_form, text="Fecha inicio:", font=("Arial", 14)).grid(
            row=4, column=0, padx=20, pady=10, sticky="w")
        self.date_inicio = DateEntry(
            self.frame_form, width=20, font=("Arial", 12),
            date_pattern="dd/mm/yyyy", background="#1f6aa5", foreground="white")
        self.date_inicio.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        # Botón registrar
        ctk.CTkButton(
            self, text="Registrar póliza",
            command=self.registrar,
            font=("Arial", 16, "bold"), height=45, width=250
        ).pack(pady=15)

        # Label para mostrar resultado
        self.label_resultado = ctk.CTkLabel(
            self, text="", font=("Arial", 14), text_color="#5dade2")
        self.label_resultado.pack(pady=5)

        # Label contador
        self.label_contador = ctk.CTkLabel(
            self, text="Pólizas registradas: 0",
            font=("Arial", 12), text_color="gray")
        self.label_contador.pack(pady=5)

  
    # MÉTODO: se ejecuta cuando el usuario presiona "Registrar póliza"
    def registrar(self):
        # 1) Leer los datos de los campos
        titular = self.entry_titular.get().strip()
        edad_txt = self.entry_edad.get().strip()
        tipo = self.combo_tipo.get()
        prima_txt = self.entry_prima.get().strip()
        fecha = self.date_inicio.get()

        # 2) Validar que no haya campos vacíos
        if titular == "" or edad_txt == "" or prima_txt == "":
            messagebox.showwarning("Campos vacíos", "Por favor llena todos los campos.")
            return

        # 3) Validar que edad y prima sean números
        try:
            edad = int(edad_txt)
            prima = float(prima_txt)
        except ValueError:
            messagebox.showerror("Datos inválidos",
                                "La edad debe ser un número entero y la prima un número.")
            return

        # 4) Crear la póliza del tipo correcto (POLIMORFISMO)
        clase_poliza = TIPOS_POLIZA[tipo]
        poliza = clase_poliza(titular, edad, prima, fecha)

        # 5) Guardar en memoria Y en Excel
        self.polizas.append(poliza)
        self.excel.guardar_poliza(poliza)    # guarda en datos/polizas.xlsx

        # 6) Mostrar resultado en la ventana
        mensual = poliza.calcular_prima_mensual()
        self.label_resultado.configure(
            text=f"✓ {tipo} registrada para {titular} · Prima: ${mensual:,.2f}")
        self.label_contador.configure(
            text=f"Pólizas registradas: {len(self.polizas)}")

        # 7) Limpiar los campos para el siguiente registro
        self.entry_titular.delete(0, "end")
        self.entry_edad.delete(0, "end")
        self.entry_prima.delete(0, "end")

        # 8) Imprimir en consola para confirmar
        print(poliza)