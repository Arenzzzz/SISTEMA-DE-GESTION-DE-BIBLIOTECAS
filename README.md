SISTEMA DE GESTIÓN DE BIBLIOTECAS:

- Descripción del proyecto:
Este proyecto implementa un sistema básico de gestión de biblioteca orientado a objetos en Python. Permite la creación y validación de libros digitales y físicos con atributos específicos (título, autor, año de publicación, formato o número de páginas). Además, incluye una clase Biblioteca que organiza y gestiona colecciones diferenciadas de libros digitales y físicos, permite mostrar el inventario completo y buscar libros por autor.
Se incorporan funciones para validar entradas y un mecanismo para manejar errores durante la creación de objetos, asegurando que los datos sean correctos y evitando interrupciones inesperadas.

- ¿Cómo ejecutar el programa?
  1. Crear instancias de libros
      Hay dos tipos de libros, por lo que debes crear instancias de las clases correspondientes:
  
      a) Libro Digital (LibroDigital)
          Parámetros:
            titulo: texto no vacío (ej. 'Divina Comedia')
            autor: texto no vacío (ej. 'Dante Alighieri')
            anio_p: año de publicación como entero o texto que pueda convertirse a entero (ej. '1300' o 1300)
            formato: texto no vacío que indica el formato digital (ej. 'PDF', 'EPUB')

      b) Libro Físico (LibroFisico)
          Parámetros:
            titulo: texto no vacío (ej. 'Rusticatio Mexicana')
            autor: texto no vacío (ej. 'Rafael Landívar')
            anio_p: año de publicación como entero o texto convertible a entero (ej. '1782')
            n_paginas: número entero de páginas (ej. 248)
     
  3. Manejo de errores al crear libros
      Para evitar que datos incorrectos detengan el programa, se debe usar la función (crear_con_manejo_errores) que intenta crear la instancia y captura errores de validación:
         Ejemplos:
               L1 = crear_con_manejo_errores(LibroDigital, 'Divina Comedia', 'Dante Alighieri', 'mil trescientos', 'PDF')
               L2 = crear_con_manejo_errores(LibroFisico, 'Rusticatio Mexicana', 'Rafael Landívar', '1782', '248')
     
  5. Crear la biblioteca y agregar libros
      Se crea una instancia de la clase Biblioteca para iniciarla:
         biblioteca = Biblioteca()

     Luego de ello ya se pueden utilizar los métodos de la clase Biblioteca:
       - AGREGAR LIBROS:
         Se validará si cada libro registrado anteriormente no tenga errores para hacer uso de los métodos de Biblioteca
             if libro_digital:
                biblioteca.agregar_libro(libro_digital)
             if libro_fisico:
                biblioteca.agregar_libro(libro_fisico)
         
       - MOSTRAR LIBROS:
         biblioteca.mostrar_biblioteca()
         
       - BUSCAR LIBROS POR AUTOR:
         Para buscar libros de un autor específico (el nombre no es sensible a mayúsculas/minúsculas):
             biblioteca.buscar_libro('Dante Alighieri')
     
- Reflexión de las ventajas de usar super() en el sistema:
El uso de super() en las clases hijas LibroDigital y LibroFisico facilita la reutilización del código definido en la clase base Libro. Esto permite que los atributos comunes (como título, autor y año de publicación) se inicialicen y validen una sola vez, evitando duplicación y posibles errores.
Además, al invocar super() para llamar a métodos heredados (como mostrar_info), se mantiene una estructura ordenada y modular, donde cada clase se encarga únicamente de sus detalles específicos, promoviendo la mantenibilidad y escalabilidad del código.
