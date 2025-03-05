# Usa una imagen oficial de Python
FROM python:3.10

# Crea un usuario sin privilegios y usa /app como directorio de trabajo
RUN useradd -m appuser
WORKDIR /app

# Copia primero solo el archivo de dependencias para aprovechar la caché de Docker
COPY --chown=appuser:appuser requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia únicamente los archivos y directorios relevantes del código
COPY --chown=appuser:appuser Gestion_Paquete /app/Gestion_Paquete
COPY --chown=appuser:appuser main.py /app/main.py

# Cambia al usuario sin privilegios
USER appuser

# Comando de ejecución
CMD ["python", "main.py"]
