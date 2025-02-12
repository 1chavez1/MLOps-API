# API de Análisis de Sentimientos con Flask

## Descripción del Proyecto
Este proyecto tiene como objetivo desarrollar una API utilizando Flask para realizar inferencia con un modelo de análisis de sentimientos proporcionado por otro equipo de trabajo encargado de la creación y entrenamiento de modelos (Model Building). Este sistema está diseñado para acelerar el proceso de análisis de las reseñas de productos, optimizando la capacidad de la empresa para tomar decisiones basadas en los comentarios de los clientes.

## Contexto
En este flujo de trabajo, el equipo de Model Building entrena y ajusta un modelo de machine learning especializado para el análisis de sentimientos. Una vez entrenado, el modelo es entregado al equipo de Model Inference para integrarlo en un entorno productivo a través de una API. Este proyecto aborda esa segunda etapa, proporcionando una solución escalable, eficiente y fácil de usar para consumir predicciones del modelo.

## Consideraciones de diseño
Este proyecto está diseñado como un prototipo funcional para demostrar habilidades técnicas en un entorno controlado. Actualmente, la API es sincrónica, lo que es adecuado para un único usuario que realiza solicitudes de análisis de sentimientos.

En un entorno de producción con múltiples usuarios o altos volúmenes de solicitudes, se recomienda implementar una arquitectura asíncrona

## Características del Proyecto
1. **API RESTful**: Diseñada con Flask, siguiendo buenas prácticas de desarrollo de software para garantizar escalabilidad y mantenibilidad.
2. **Predicciones en Tiempo Real**: Permite realizar análisis de sentimiento de las reseñas de productos en tiempo real.
3. **Flexibilidad y Extensibilidad**: El sistema está diseñado para ser modular, facilitando la integración de nuevos modelos en el futuro.
4. **Optimizado para Producción**: Se consideran principios de MLOps, como la gestión de versiones del modelo, manejo de errores y logging.

## Tecnologías Utilizadas
- **Flask**: Framework principal para la creación de la API.
- **Pydantic**: Validación y serialización de datos para garantizar entradas seguras.
- **PyTorch**: Herramienta utilizada para cargar el modelo preentrenado.
- **Docker**: Para contenerizar la aplicación y facilitar su despliegue.
- **Postman**: Para pruebas y validación de los endpoints de la API.

## Estructura del Proyecto
```
|-- app/
|   |-- run.py        # Código de la API (Flask).
|   |
|   |-- api/
|   |   |-- prediction.py # Codigo de blueprint
|   |  
|   |-- config/
|   |   |-- __init__.py      # Inicializador de configuración.
|   |   |-- .env             # Variables de entorno.
|   |   |-- model.py         # Configuración del modelo.
|   |
|   |-- model/
|   |   |-- Sentiment_model_complete.pth  # Modelo entrenado.
|   |   |-- vectorizer.pkl               # Vectorizador de texto.
|   |
|   |-- schema/
|   |   |-- review_analysis.py   # Esquema Pydantic.
|   |
|   |-- services/
|   |   |-- __init__.py
|   |   |-- model_inference.py  # Inferencia del modelo.
|
|-- Dockerfile              # Archivo de configuración para Docker.
|-- Makefile                # Archivo para automatización
|-- poetry.lock             # Lockfile de Poetry.
|-- pyproject.toml          # Archivo principal de Poetry.
|-- README.md               # Documentación del proyecto.
|-- setup.cfg               # Configuración adicional de Python.
```
- **app/**: Contiene el código principal de la API.
- **Dockerfile**: Archivo para contenerizar la aplicación.
- **pyproject.toml**: Dependencias del proyecto.
- **README.md**: Documentación del proyecto.

## Instalación y Ejecución
### Requisitos Previos
- Python 3.10+
- Docker (opcional, para despliegue)

### Pasos para Ejecutar Localmente
1. Clona este repositorio:
   ```bash
   git clone https://github.com/1chavez1/MLOps-API.git
   cd project
   ```

2. Instala las dependencias:
Se recomienda utilizar un entorno virtual para aislar el proyecto. Si estás gestionando las dependencias con `Poetry`, sigue estos pasos:
Ejecuta el siguiente comando para instalar todas las dependencias definidas en el archivo `pyproject.toml`:
  ```bash
  poetry install
```

3. Ejecuta la aplicación:
   ```bash
   poetry run python app/run.py
   ```

4. Accede a la API en `http://localhost:5000`
Esta API tiene expuesto el puerto 8080 para uso de Google Cloud Run, cambia este puerto por 5000 para pruebas unitarias.

### Uso de Docker
1. Construye la imagen de Docker:
   ```bash
   docker build -t sentiment-analysis-api .
   ```

2. Ejecuta el contenedor:
   ```bash
   docker run -p 5000:5000 sentiment-analysis-api
   ```

## Endpoints
### POST `/api/prediction`
Realiza el análisis de sentimiento de una lista de reseñas.

#### Request
```json
{
  "review": [
    "Este producto es increíble! Me encanta."
  ]
}
```

#### Response
```json
{
  "Predicted Sentiments": [
    {"review_text": "Este producto es increíble! Me encanta.", "sentiment": "positivo"}
  ]
}
```
