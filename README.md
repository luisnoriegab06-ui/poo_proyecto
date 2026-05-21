Sistema de Gestión - Concesionaria de Autos

Proyecto Final de Programación Orientada a Objetos (POO) - 2do Semestre.

Requisitos del Proyecto Cumplidos

* Arquitectura MVC: Proyecto organizado correctamente en las carpetas modelo/, datos/ y vista/.
* Archivos __init__.py: Incluidos en cada carpeta de código para la correcta modularización.
* Punto de entrada limpio: Archivo main.py en la raíz con menos de 5 líneas de código para arrancar el sistema.
* Entorno Virtual: Configurado correctamente e ignorado en el repositorio mediante el archivo .gitignore.
* requirements.txt: Archivo actualizado con las dependencias necesarias (openpyxl y tkcalendar).

Programación Orientada a Objetos (POO)

* Clases Propias: Implementación de clases (Cliente, Auto, Venta, ControladorConcesionaria).
* Encapsulamiento: Atributos privados (self.__nombre, etc.) con sus Getters y Setters (@property).
* Herencia: Clase hija Cliente que hereda de la clase padre mediante el uso de super().__init__().
* Clase Abstracta: Uso de la librería abc con la clase Persona y su método abstracto @abstractmethod.
* Polimorfismo: Aplicado correctamente sin usar la condicional (if).

Persistencia de Datos e Interfaz

* Interfaz Gráfica: Desarrollada en tkinter con ventanas funcionales, uso de formularios con ComboBox, DateEntry y tablas dinámicas (Treeview).
* Validaciones: Control de campos vacíos y formatos numéricos correctos con alertas en pantalla (messagebox).
* Persistencia: Guardado, lectura automática al abrir y eliminación de registros directamente en un archivo de Excel (concesionaria.xlsx) usando la librería openpyxl.

Instrucciones para compilar el Ejecutable (.exe)
1. Se instaló la herramienta en el entorno virtual con el comando: 
   pip install pyinstaller
2. Se ejecutó el comando de compilación apuntando al punto de entrada del programa: 
   pyinstaller --windowed --onefile main.py
   Nota: Se usó --windowed para ocultar la consola del sistema y --onefile para generar un único archivo distribuible.
3. El archivo final .exe se genera automáticamente dentro de la carpeta /dist.