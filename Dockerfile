# Usa la imagen oficial de Python
FROM python:3.10

# Crea un usuario sin privilegios
RUN useradd -m appuser

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos
COPY Gestion_Paquete /app/Gestion_Paquete
COPY requirements.txt /app/

# Ajusta los permisos después de copiar
RUN chown -R appuser:appuser /app

# Cambia al usuario sin privilegios
USER appuser

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando de ejecución
CMD ["python", "Gestion_Paquete/main.py"]
