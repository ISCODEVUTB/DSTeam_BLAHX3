# Usar la imagen base de Python
FROM python:3.10

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de dependencias primero (para optimizar la caché de Docker)
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente al contenedor
COPY . .

# Establecer la carpeta `Gestion` como directorio de trabajo
WORKDIR /app/Gestion

# Ejecutar el script principal
CMD ["python", "main.py"]
