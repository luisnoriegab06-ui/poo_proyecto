import tkinter as tk
from vista.ventana_login import VentanaLogin
from vista.app_concesionaria import AppConcesionaria

def iniciar_aplicacion_principal():
    # Limpia el login de la pantalla para dar paso a la app
    for widget in root.winfo_children():
        widget.destroy()
    
    # Arranca tu ventana principal con el nombre correcto
    app = AppConcesionaria(root)

if __name__ == "__main__":
    root = tk.Tk()
    
    # El sistema arranca obligatoriamente por la pantalla de seguridad
    login = VentanaLogin(root, on_success=iniciar_aplicacion_principal)
    
    root.mainloop() 