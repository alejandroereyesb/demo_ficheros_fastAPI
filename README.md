# Demo FastAPI File Management

## Tecnologías utilizadas
- **FastAPI**: Framework para construir APIs rápidas y modernas con Python.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación FastAPI.
- **Python**: Lenguaje de programación utilizado.
- **Zipfile**: Módulo estándar de Python para compresión de archivos.

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/alejandroereyesb/demo_ficheros_fastAPI.git
   cd demo_ficheros_fastAPI
   ```

2. **Crear un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**:
   ```bash
   python app.py
   ```

5. **Acceder a la documentación interactiva**:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Uso de la API

### Endpoints principales

1. **Subir un archivo**:
   - **POST** `/upload/`
   - Enviar uno o más archivos en el cuerpo de la solicitud.

2. **Subir múltiples archivos**:
   - **POST** `/upload-multiple/`
   - Enviar múltiples archivos en el cuerpo de la solicitud.

3. **Listar archivos**:
   - **GET** `/files/`
   - Devuelve una lista de todos los archivos en el directorio de subida.

4. **Descargar un archivo**:
   - **GET** `/files/{file_name}`
   - Descarga un archivo específico.

5. **Descargar un archivo como ZIP**: como archivos no encontrados o fallos en la compresión.
   - **GET** `/files/{file_name}/download-zip/`
   - Descarga un archivo específico en formato ZIP.

6. **Actualizar un archivo**:
   - **PUT** `/files/{file_name}`
   - Reemplaza un archivo existente con uno nuevo.

7. **Eliminar un archivo**:
   - **DELETE** `/files/{file_name}`
   - Elimina un archivo específico.

## Notas adicionales
- Los archivos subidos se almacenan en el directorio `uploaded_files`.
- Asegúrate de que el directorio tenga permisos de escritura.
- La API incluye manejo básico de errores para operaciones