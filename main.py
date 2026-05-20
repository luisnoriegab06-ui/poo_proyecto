import sys
import os
import tkinter as tk

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


from vista.app_concesionaria import AppConcesionaria

if __name__ == "__main__":
    
    root = tk.Tk()
    app = AppConcesionaria(root)
    
    root.mainloop()