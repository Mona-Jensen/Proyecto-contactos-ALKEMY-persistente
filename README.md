Este es un proyecto educativo de ALKEMY que implementa un sistema de gestión de contactos con persistencia de datos. El proyecto fue creado por Gianina Jensen y contiene la lógica necesaria para crear, almacenar y administrar una lista de contactos utilizando almacenamiento persistente en archivos JSON. El repositorio está en estado inicial con un único commit.

Puntos de Función Principal
Gestión de contactos (crear, leer, actualizar, eliminar)
Persistencia de datos en formato JSON
Interfaz de usuario para interactuar con los contactos
Separación de responsabilidades entre modelos y lógica de gestión
Almacenamiento permanente de información de contactos
Stack Tecnológico
Python (lenguaje de programación principal)
JSON (formato de almacenamiento de datos)
Modelos de datos orientados a objetos (OOP)

1. Documentación Técnica
Estructura del Proyecto y Módulos El proyecto está organizado de manera modular, separando la definición de datos de la lógica de negocio. Los archivos principales incluyen:
• contacto_persistente.py: Define el modelo de datos del contacto utilizando Programación Orientada a Objetos (OOP).
• gestion_persistente.py: Contiene la lógica para administrar la lista de contactos y la persistencia de datos.
• main_persistente.py: Actúa como el punto de entrada de la aplicación, gestionando la interfaz de usuario por consola.
• contactos.json: Archivo utilizado para el almacenamiento permanente de la información.
• requirements.txt: Lista las dependencias necesarias para el entorno.
Arquitectura La aplicación sigue un enfoque de separación de responsabilidades, donde los modelos y la lógica de gestión residen en módulos independientes para facilitar el mantenimiento y la escalabilidad. Utiliza JSON como motor de persistencia, permitiendo que los datos se conserven tras cerrar el programa.
Instrucciones de Ejecución
1. Asegúrese de tener instalado Python (versión 3.6 o superior recomendada).
2. Clonar el repositorio o descargar los archivos fuente.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar la aplicación con el comando: python main_persistente.py.

2. Prototipo Funcional
El sistema permite realizar las operaciones fundamentales de gestión de información (CRUD) a través de una interfaz interactiva en la consola:
• Agregar contactos: Captura nombre, teléfono, correo y dirección mediante la función input().
• Editar y eliminar: Permite localizar un registro existente para modificar sus atributos o removerlo de la base de datos JSON.
• Buscar contactos: Implementa lógica de búsqueda eficiente por nombre o número de teléfono.
• Organización: Los datos se estructuran internamente mediante listas y diccionarios antes de ser serializados a JSON.

3. Informe de Pruebas
Metodología Se implementaron pruebas unitarias utilizando el módulo estándar de Python unittest, reflejado en el archivo import unittest.py del repositorio.
Pruebas Realizadas
• Registro de contactos: Validación de que los nuevos objetos se crean correctamente con todos sus atributos.
• Búsqueda: Verificación de que el sistema retorna los resultados correctos al filtrar por nombre o teléfono.
• Persistencia: Comprobación de que los datos escritos en contactos.json se recuperan íntegramente al reiniciar la aplicación.
Resultados Obtenidos La presencia del módulo de pruebas garantiza que las funcionalidades principales operan según los requerimientos técnicos establecidos, asegurando un código robusto y confiable.


