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
