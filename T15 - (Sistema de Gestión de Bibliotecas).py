# Hecho por: ARENZ PELÁEZ - 1556425

# Funcuiones de validación de entrada de datos
def validar_espacios(texto, nombre_campo):  # Valida que el texto no esté vacío
    texto = str(texto).strip()
    if not texto:
        raise ValueError(f"El campo '{nombre_campo}' no puede estar vacío.")
    return texto

def validar_entero(valor, nombre_campo):  # Valida que el valor sea dígito
    valor_str = str(valor).strip()
    if not valor_str.isdigit():
        raise ValueError(f"El campo '{nombre_campo}' debe ser un número entero.")
    return int(valor_str)

# Clase padre para el ingreso de libros y el métoodo principal para mostrar la información
class Libro:
    def __init__(self, titulo, autor, anio_p):
        # Validación de cada dato ingresado
        self.titulo = validar_espacios(titulo, "Título")
        self.autor = validar_espacios(autor, "Autor").title()
        self.anio_p = validar_entero(anio_p, "Año de publicación")

    def mostrar_info(self):
        print(f'{self.titulo.upper()}')
        print(f'\tAutor: {self.autor} \n\tAño de publicación: {self.anio_p}')

# Clases hijas para libros digitales y físicos, con sus atributos y métodos específicos
class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio_p, formato):
        super().__init__(titulo, autor, anio_p)
        self.formato = validar_espacios(formato, "Formato") # Valida que el formato no esté vacío

    def mostrar_info(self):
        super().mostrar_info()
        print(f'\tFormato: {self.formato}')
        
class LibroFisico(Libro):
    def __init__(self, titulo, autor, anio_p, n_paginas):
        super().__init__(titulo, autor, anio_p)
        self.n_paginas = validar_entero(n_paginas, "Número de páginas")

    def mostrar_info(self):
        super().mostrar_info()
        print(f'\tNúmero de páginas: {self.n_paginas}')

# Clase para gestionar la biblioteca, agregar, mostrar y buscar libros      
class Biblioteca:
    def __init__(self):
        # Lista de diccionarios para almacenar libros digitales y físicos
        self.libros = [
                {
                    'Libros Digitales': []
                },
                {
                    'Libros Físicos': []
                }
            ]
        
    def agregar_libro(self, libro):
        for tipo in self.libros:
            if isinstance(libro, LibroDigital) and 'Libros Digitales' in tipo:
                tipo['Libros Digitales'].append(libro)

            elif isinstance(libro, LibroFisico) and 'Libros Físicos' in tipo:
                tipo['Libros Físicos'].append(libro)
                
    def mostrar_biblioteca(self):
        for libros in self.libros:
            for tipo, detalles in libros.items():
                print(f'\n{tipo}:')
                if len(detalles) > 0:
                    for l in detalles:
                        l.mostrar_info()
                else: 
                    print('No hay libros registrados')
    
    def buscar_libro(self, autor):
        autor = autor.title()
        print(f'\nBúsqueda de libros por autor: {autor}')
        encontrado = False
        for libros in self.libros:
            for tipo, detalles in libros.items():
                for l in detalles:
                    if l.autor == autor:
                        encontrado = True
                        l.mostrar_info()
                        print(f'\tCategoría: {tipo}')
                        
        if not encontrado:
            print(f'Libros de {autor} no encontrados, verifique escritura')

# Función para manejar errores al crear instancias de libros
def crear_con_manejo_errores(clase, *args, **kwargs):
    # Ingresa los datos y maneja errores si los hay retorn
    try:
        return clase(*args, **kwargs)
    except ValueError as e:
        print(f"Error al crear {clase.__name__}: {e}")
        return False

print('=== SISTEMA DE GESTIÓN DE BIBLIOTECA ===')

# Creación de libros y validandoo errores con la función anterior
L1 = crear_con_manejo_errores(LibroDigital, 'Divina Comedia', 'Dante Alighieri', 'mil trescientos', 'PDF')
L2 = crear_con_manejo_errores(LibroFisico, 'Rusticatio Mexicana', 'Rafael Landívar', '1782', '248')

# Inicialización de la clase Biblioteca
B = Biblioteca()

# Solo agrega los libros si fueron creados sin errores
if L1:
    B.agregar_libro(L1)
if L2:
    B.agregar_libro(L2)

# Mostrar la biblioteca y realizar búsquedas
B.mostrar_biblioteca()
B.buscar_libro('Dante Alighieri')   # Búsqueda errónea ya que no se agregó el libro por manejo de errores
B.buscar_libro('RAFAEL LANDÍVAR')
B.buscar_libro('Arenz') # Error intencional para probar búsqueda sin resultados
