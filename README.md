# Todo App

Esta es una aplicación backend simple construida con Flask. Permite realizar operaciones CRUD (crear, leer y eliminar) sobre una lista de tareas almacenadas en un archivo JSON.

## Cómo usar

1. Instala Flask si no lo tienes:
   ```bash
   pip install flask
   ```

2. Ejecuta la app:
   ```bash
   python app/main.py
   ```

3. Accede a las rutas disponibles:
   - `GET /tasks`: Obtener todas las tareas
   - `POST /tasks`: Agregar una nueva tarea (enviar JSON)
   - `DELETE /tasks/<índice>`: Eliminar una tarea por su índice

## Estructura de carpetas

```
todo-app/
│
├── app/
│   ├── main.py        # Backend con Flask
│   └── tasks.json     # Archivo de almacenamiento de tareas
│
└── README.md
```

