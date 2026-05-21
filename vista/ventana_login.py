import tkinter as tk
from tkinter import messagebox

class VentanaLogin:
    def __init__(self, root, on_success):
        self.root = root
        self.on_success = on_success
        self.root.title("Acceso al Sistema - Seguridad")
        self.root.geometry("350x220")
        
        # Intentar centrar la ventana en pantalla
        self.root.eval('tk::PlaceWindow . center')

        # Contenedor principal para que se vea ordenado
        frame = tk.Frame(root, padx=20, pady=20)
        frame.pack(expand=True, fill="both")

        tk.Label(frame, text="Iniciar Sesión", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(frame, text="Usuario:").pack(anchor="w")
        self.txt_user = tk.Entry(frame, width=30)
        self.txt_user.pack(pady=5)

        tk.Label(frame, text="Contraseña:").pack(anchor="w")
        self.txt_pass = tk.Entry(frame, show="*", width=30)
        self.txt_pass.pack(pady=5)

        tk.Button(frame, text="Ingresar al Sistema", command=self.validar_acceso, bg="#2196F3", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5).pack(pady=15)

    def validar_acceso(self):
        # Credenciales fijas exigidas para la entrega de seguridad
        if self.txt_user.get() == "admin" and self.txt_pass.get() == "1234":
            self.on_success()
        else:
            messagebox.showerror("Error de Autenticación", "Usuario o contraseña incorrectos.")