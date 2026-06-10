# Gestor de Lista de Contactos para ACME Solutions

## Descripción
Este proyecto es una aplicación desarrollada en Python para gestionar contactos y usuarios dentro de la empresa ACME Solutions.

El sistema permite:

- Inicio de sesión de usuarios.
- Registro de usuarios.
- Registro de contactos.
- Listar contactos.
- Buscar contactos.
- Actualizar contactos.
- Eliminar contactos.
- Persistencia de datos mediante JSON.



## Tecnologías utilizadas

- Python
- JSON
- Visual Studio Code



## Estructura del proyecto



Proyecto_Python/

├── app.py
├── modules/
│   ├── core.py
│   ├── utils.py
│   ├── messages.py
│   ├── crud_users.py
│   └── crud_contacts.py
│
└── data/
    └── agenda.json




## Explicación de archivos

### app.py
Archivo principal del sistema.
Controla:
- Login
- Menú principal
- Navegación entre opciones

### core.py
Contiene la lógica principal del sistema:
- Inicio de sesión
- Validación de usuarios

### utils.py
Funciones reutilizables:
- Leer JSON
- Guardar JSON
- Validar inputs

### crud_users.py
Maneja el CRUD de usuarios:
- Registrar usuarios

### crud_contacts.py
Maneja el CRUD de contactos:
- Registrar
- Listar
- Buscar
- Actualizar
- Eliminar

### messages.py
Muestra los menús y mensajes del sistema.

### agenda.json
Actúa como base de datos del sistema.



## Funcionalidades implementadas

### Login
El sistema solicita:
- Correo corporativo
- Contraseña

Solo usuarios válidos pueden ingresar.



### Registro de usuarios
Solo el administrador puede:
- Crear nuevos usuarios
- Asignar roles



### Registro de contactos
Permite almacenar:
- ID
- Nombre
- Teléfono
- Email
- Dirección
- Tipo de contacto
- Notas



### Listado de contactos
Muestra los contactos en forma de tabla en consola.



### Búsqueda de contactos
Se puede buscar por:
- ID
- Nombre
- Tipo



### Actualización de contactos
Permite modificar únicamente los datos necesarios.
Si el usuario presiona ENTER, el valor anterior se conserva.



### Eliminación de contactos
Permite eliminar contactos con confirmación previa.



## Persistencia de datos

Toda la información se almacena en:



data/agenda.json



Esto permite conservar la información incluso después de cerrar el programa.



## Cómo ejecutar el proyecto

1. Abrir la carpeta del proyecto en Visual Studio Code.
2. Abrir la terminal.
3. Ejecutar:

```bash
python app.py
```



## Usuario administrador inicial

Correo:
admin@acmesolutions.com

Contraseña:
admin123

