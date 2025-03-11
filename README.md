# DSTeam_BLAHX3
# Sistema Gestión de Paquetes

## Descripción
El Sistema de Gestión de Paquetes es un programa desarrollado en Python que permite gestionar envíos de paquetes de manera eficiente. Proporciona herramientas para registrar, actualizar, eliminar y clasificar paquetes, así como gestionar la trazabilidad de los envíos, registrar y autenticar usuarios, y administrar facturación y pagos.

## Estado del Proyecto
✅ Proyecto terminado
Todas las pruebas realizadas al programa funcionaron con normalidad.

## Tecnologías Utilizadas
- **Lenguaje:** Python
- **Frameworks/Bibliotecas:**
  - Flask (para el desarrollo del backend)
  - Flask-WTF (para manejo de formularios)
  - Flask-SeaSurf (para protección contra CSRF)
- **Docker:** Utilizado para contenedorización y despliegue
- **SonarQube:** Implementado para análisis de calidad del código y cobertura de pruebas

## Instalación y Dependencias
Para ejecutar el sistema, se deben instalar las siguientes dependencias:
```sh
pip install -r requirements.txt
```
El archivo `requirements.txt` debe incluir las siguientes bibliotecas:
```sh
bcrypt==4.3.0
pytest
pylint==3.3.4
Flask==3.1.0
Flask-SeaSurf==1.1.1
pytest-cov
Flask-WTF
psycopg2==2.9.6
```
Para ejecutar el sistema:
```sh
python main.py
```
Para construir y desplegar con Docker:
```sh
docker build -t mi-paquete .
docker run -p 8080:8080 mi-paquete
```
Para realizar análisis de calidad con SonarQube:
```sh
pytest --cov=src --cov-report=xml --cov-report=term
```

## Uso de Docker
El sistema se ejecuta en un contenedor Docker. A continuación, se detallan los archivos utilizados para la configuración del contenedor.

### Archivo `.dockerignore`
Este archivo excluye archivos y directorios innecesarios en la imagen de Docker.
```
__pycache__/
.env
*.pyc
*.pyo
*.pyd
.vscode/
.idea/
.DS_Store
.git/
```

### Archivo `Dockerfile`
El `Dockerfile` define la configuración del contenedor para ejecutar el sistema.
```dockerfile
FROM python:3.9-slim

# Crea un usuario no-root (por ejemplo, "appuser")
RUN adduser --disabled-password --gecos '' appuser

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos y instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY main.py .
COPY src/ ./src/

# Cambia al usuario no-root
USER appuser

# Expone el puerto que usa el sistema
EXPOSE 8080

# Comando para iniciar el sistema
CMD ["python", "main.py"]
```

## Características del Sistema
### Registro de Usuarios
Los usuarios deben registrarse antes de acceder a las funcionalidades del sistema. Existen diferentes roles dentro del programa.

### Gestor de Paquetes
Permite registrar nuevos paquetes, especificando dimensiones, peso y tipo (básico, estándar o dimensionado).

### Creación de Envíos
Los envíos son creados por los usuarios que realizan los pedidos.

### Trazabilidad
Se puede hacer seguimiento del estado de los paquetes desde su registro hasta la entrega.

### Facturación y Pagos
El sistema genera facturas y permite realizar pagos mediante métodos seguros.

## Gestión de Ubicaciones
El sistema implementa la clase `Location`, que permite almacenar y gestionar la información de ubicaciones asociadas a envíos y destinatarios.

### Características de la Clase `Location`
- Almacena información sobre país, departamento, ciudad, dirección y código postal.
- Genera un identificador único (UUID) para cada ubicación.
- Valida el código postal para asegurar que sea un valor numérico positivo.
- Proporciona métodos getter y setter para modificar los atributos de manera controlada.

**Ejemplo de uso:**
```python
from location import Location

ubicacion = Location("Colombia", "Bolivar", "Cartagena", "CRA 10 #25-30", "Apt 301", 130001)
print(ubicacion)
```

## Estados y Tipos de Paquetes
El sistema maneja diferentes estados para los pedidos y clasificaciones para los paquetes.

### Estados de los Pedidos (`OrderStatus`)
Los pedidos pueden encontrarse en uno de los siguientes estados:
- **Pending:** El pedido ha sido creado pero aún no ha sido procesado.
- **Shipped:** El pedido ha sido enviado al destinatario.
- **Delivered:** El pedido ha sido entregado con éxito.
- **Canceled:** El pedido ha sido cancelado y no será enviado.

**Ejemplo de uso:**
```python
from order_status import OrderStatus

estado = OrderStatus.PENDING
print(f"El estado actual del pedido es: {estado.value}")
```

### Tipos de Paquete (`PackageTypes`)
Los paquetes pueden clasificarse en:
- **Básico (`basico`)**: Paquetes de tamaño y peso estándar.
- **Estándar (`estandar`)**: Paquetes de mayor tamaño o peso medio.
- **Dimensionado (`dimensionado`)**: Paquetes con dimensiones fuera de lo común.

**Ejemplo de uso:**
```python
from package_types import PackageTypes

tipo_paquete = PackageTypes.ESTANDAR
print(f"El tipo de paquete seleccionado es: {tipo_paquete.value}")
```

## Integración y Despliegue
El proyecto cuenta con integración continua a través de GitHub Actions:
- **Docker Build and Deploy:** Automatiza la construcción y despliegue en Docker Hub.
- **SonarQube Analysis:** Ejecuta pruebas automáticas y análisis de calidad del código con cobertura de pruebas.

## Colaboradores
- Jesus Julio
- Ana Meza
- Isabella Ordozgoitia
- Kathy Otero
- Alejandro Villareal

## Licencia
Este proyecto está licenciado bajo la Licencia Pública General GNU v3.0. Para más detalles, consulta el siguiente enlace: [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).



