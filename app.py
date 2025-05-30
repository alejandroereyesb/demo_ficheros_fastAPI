from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, StreamingResponse  # Importar para enviar el archivo ZIP como respuesta
import os
import uvicorn
import zipfile  # Importar módulo para compresión
from io import BytesIO  # Importar para manejar datos en memoria

app = FastAPI()

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Ruta de bienvenida
@app.get("/")
async def root():
    return {
        "message": "Bienvenido a la API de gestión de ficheros con FastAPI",
        "docs": "Visita /docs para la documentación interactiva (Swagger UI)",
        "redoc": "Visita /redoc para la documentación alternativa (ReDoc)"
    }

# Crear (Subir un fichero)
@app.post("/upload/")
async def upload_files(files: list[UploadFile] = File(...)):
    try:
        uploaded_files = []
        for file in files:
            file_path = os.path.join(UPLOAD_DIR, file.filename)
            with open(file_path, "wb") as f:
                f.write(await file.read())
            uploaded_files.append(file.filename)
        return {"message": "Files uploaded successfully.", "files": uploaded_files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading files: {str(e)}")

# Crear (Subir múltiples ficheros)
@app.post("/upload-multiple/")
async def upload_multiple_files(files: list[UploadFile] = File(...)):
    try:
        uploaded_files = []
        for file in files:
            file_path = os.path.join(UPLOAD_DIR, file.filename)
            with open(file_path, "wb") as f:
                f.write(await file.read())
            uploaded_files.append(file.filename)
        return {"message": "Multiple files uploaded successfully.", "files": uploaded_files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading multiple files: {str(e)}")

# Leer (Descargar un fichero)
@app.get("/files/{file_name}")
async def read_file(file_name: str):
    try:
        file_path = os.path.join(UPLOAD_DIR, file_name)
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not found")
        return FileResponse(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")

# Descargar un fichero en formato ZIP
@app.get("/files/{file_name}/download-zip/")
async def download_file_as_zip(file_name: str):
    try:
        file_path = os.path.join(UPLOAD_DIR, file_name)
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not found")
        
        # Crear un archivo ZIP en memoria
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zipf:
            zipf.write(file_path, arcname=file_name)
        zip_buffer.seek(0)  # Volver al inicio del buffer
        
        return StreamingResponse(
            zip_buffer,
            media_type="application/zip",
            headers={"Content-Disposition": f"attachment; filename={file_name}.zip"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error downloading file as ZIP: {str(e)}")

# Obtener la lista de todos los ficheros
@app.get("/files/")
async def list_files():
    try:
        files = os.listdir(UPLOAD_DIR)
        return {"files": files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error listing files: {str(e)}")

# Actualizar (Reemplazar un fichero)
@app.put("/files/{file_name}")
async def update_file(file_name: str, file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file_name)
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not found")
        with open(file_path, "wb") as f:
            f.write(await file.read())
        return {"message": f"File '{file_name}' updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating file: {str(e)}")

# Eliminar (Borrar un fichero)
@app.delete("/files/{file_name}")
async def delete_file(file_name: str):
    try:
        file_path = os.path.join(UPLOAD_DIR, file_name)
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not found")
        os.remove(file_path)
        return {"message": f"File '{file_name}' deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting file: {str(e)}")



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)