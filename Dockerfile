# Usa la imagen oficial de Python
FROM python:3.10

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia solo la carpeta donde está el código y el archivo de dependencias
COPY Gestion_Paquete /app/Gestion_Paquete
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando de ejecución
CMD ["python", "Gestion_Paquete/main.py"]
