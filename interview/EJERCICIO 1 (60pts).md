EJERCICIO 1 (60pts)
Descripción
Vas a implementar un sistema de gestión de una biblioteca que permita registrar libros y usuarios, y manejar el préstamo y la devolución de libros. Además, debes escribir pruebas unitarias para asegurar que las funcionalidades del sistema funcionan correctamente.
Requisitos del Sistema
Clase Libro:
Atributos:
titulo (str): El título del libro.
autor (str): El autor del libro.
disponible (bool): Indica si el libro está disponible para préstamo.

Métodos:
prestar(): Marca el libro como no disponible si está disponible, y retorna True; de lo contrario, retorna False.
devolver(): Marca el libro como disponible.
Clase Usuario:
Atributos:
nombre (str): El nombre del usuario.
libros_prestados (list): Lista de libros que el usuario ha prestado.
Métodos:
prestar_libro(libro): Añade el libro a la lista de libros prestados si está disponible, y lo marca como no disponible. Retorna True si se pudo prestar el libro, y False en caso contrario.
devolver_libro(libro): Elimina el libro de la lista de libros prestados y lo marca como disponible. Retorna True si se pudo devolver el libro, y False en caso contrario.
Clase Biblioteca:
Atributos:
libros (list): Lista de libros en la biblioteca.
usuarios (list): Lista de usuarios registrados en la biblioteca.
Métodos:
agregar_libro(libro): Añade un libro a la lista de libros de la biblioteca.
registrar_usuario(usuario): Añade un usuario a la lista de usuarios de la biblioteca.
prestar_libro(titulo, usuario): Permite a un usuario prestar un libro disponible por su título. Retorna True si se pudo prestar el libro, y False en caso contrario.
devolver_libro(titulo, usuario): Permite a un usuario devolver un libro prestado por su título. Retorna True si se pudo devolver el libro, y False en caso contrario.
 
Pruebas Unitarias(20 pts +)
Debes escribir pruebas unitarias para validar las siguientes funcionalidades:
Agregar Libro: Verifica que un libro se pueda agregar a la biblioteca.
Registrar Usuario: Verifica que un usuario se pueda registrar en la biblioteca.
Prestar Libro Disponible: Verifica que un libro disponible se pueda prestar a un usuario.
Prestar Libro No Disponible: Verifica que un libro no disponible no se pueda prestar.
Devolver Libro Prestado: Verifica que un libro prestado se pueda devolver.
Devolver Libro No Prestado: Verifica que un libro que no ha sido prestado no se pueda devolver.
 
EJERCICIO 2 (20 pts)
Descripción
Vas a implementar un programa en Python que utilice asyncio para simular la ejecución de varias tareas asíncronas, cada una con una duración diferente. Además, escribirás pruebas unitarias para validar la funcionalidad del programa.
Requisitos del Sistema
Implementación de la Función Principal:
Función simular_tarea(nombre, duracion):
Función ejecutar_tareas(tareas):
Parámetros:
nombre (str) - El nombre de la tarea.
duracion (int) - La duración en segundos que la tarea debe simular estar ejecutándose.
Debe utilizar asyncio.sleep para simular el tiempo de ejecución de la tarea.
Debe retornar un mensaje indicando que la tarea se completó junto con su nombre y duración.
Parámetro: tareas (list) - Lista de tuplas, donde cada tupla contiene el nombre de la tarea y su duración en segundos.
Debe crear una lista de tareas utilizando la función simular_tarea para cada tupla en la lista.
Debe ejecutar todas las tareas concurrentemente utilizando asyncio.gather.
Debe retornar una lista con los mensajes de todas las tareas completadas.
 
 
 
EJERCICIO 3 (20 pts)
Descripción
Vas a implementar una función en Python que se conecte a la API de OpenWeatherMap para obtener el clima actual de una ciudad especificada. La función debe manejar adecuadamente las solicitudes HTTP y procesar la respuesta JSON para extraer la temperatura actual.
Requisitos
API Key:
 90wdeOHBA1N5aLYlUN9txe1Eev7NIQgZ
Instalar Requests: Asegúrate de tener instalada la librería requests para hacer las solicitudes HTTP. Puedes instalarla usando pip install requests.
Implementación de la Función:
Función obtener_clima(ciudad):
Parámetro: ciudad (str) - El nombre de la ciudad para la cual deseas obtener el clima.
Debe hacer una solicitud HTTP GET a la API de OpenWeatherMap.
Debe manejar errores HTTP y casos en los que la ciudad no sea encontrada.
Debe retornar la temperatura actual en grados Celsius si la solicitud es exitosa.
Si la solicitud falla, debe retornar un mensaje de error adecuado.
https://docs.tomorrow.io/reference/intro/getting-started
 
Getting Started
This Will help you to get Started With Tomorrow.io's APIs
 