
FROM python:3.9-slim

# Crea un usuario no-root (por ejemplo, "appuser")
RUN adduser --disabled-password --gecos '' appuser

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos y instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
# COPY . /app
COPY main.py .
COPY Gestion_Paquetes/ ./Gestion_Paquetes/

# Cambia al usuario no-root
USER appuser

# Expone el puerto que usa la aplicación
EXPOSE 7680

# Comando para iniciar la aplicación
CMD ["python", "main.py"]
