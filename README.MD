# Flask Sentiment Analysis API

## Project Description
This project aims to develop an API using Flask to perform inference part with a model of analysis of feelings provided by another team responsible for the creation and training of models (Model Building). This system is designed to speed up the process of analyzing product reviews, optimizing the company’s ability to make decisions based on customer feedback.

## Context
In this workflow, the model building team trains and adjusts specialized ML model for sentiment analysis. Once trained, the model is given to the model inference team to integrate at production environment through API. Providing scalable, efficient and user-friendly solutions to use for predictions.

## Design Considerations
This project is designed as a functional prototype to demonstrate technical skills in a controlled environment. Currently, the API is synchronous, which is suitable for a single user who makes requests for sentiment analysis.

In a production environment with multiple users or high volumes of requests, it is recommended to implement an asynchronous architecture.

## Characteristics of the Project
1. **RESTful API**: Designed with Flask, following good software development practices to ensure scalability and maintainability.
2. **Real-time predictions**: Allows for real-time sentiment analysis of product reviews.
3. **Flexibility and Extensibility**: The system is designed to be modular, facilitating the integration of new models in the future.
4. **Optimized for Production**: MLOps principles such as model version management, error handling and logging are considered.

## Technologies
- **Flask**:  Main framework for the creation of the API.
- **Pydantic**: Validation and serialization of data to ensure secure entries.
- **PyTorch**: Tool used to load the pre-trained model.
- **Docker**: To contain the application and facilitate its deployment.
- **Postman**: For testing and validation of API endpoints.

## Estructura del Proyecto
```
|-- .github/
|   |-- ci/cd.yml            # GitHub Actions CI/CD
|
|-- app/
|   |-- run.py               # API Code(Flask).
|   |
|   |-- api/
|   |   |-- prediction.py    # Blueprint Code.
|   |  
|   |-- config/
|   |   |-- __init__.py      # Init Config.
|   |   |-- .env             # Enviroments varaibles.
|   |   |-- model.py         # Model Configuration.
|   |
|   |-- model/
|   |   |-- Sentiment_model_complete.pth  # Trained Model.
|   |   |-- vectorizer.pkl                # Text vectorizer.
|   |                     # You need to create these files on your own.
|   |-- schema/
|   |   |-- review_analysis.py   # Pydantic Schema.
|   |
|   |-- services/
|   |   |-- __init__.py
|   |   |-- model_inference.py  # Model inference.
|
|-- Dockerfile              # File to contain the application.
|-- Makefile                # Archive for automation.
|-- poetry.lock             # Lockfile Poetry.
|-- pyproject.toml          # Project dependencies.
|-- README.md               # Project documentation.
|-- setup.cfg               # Additional Python configuration.
```
- **app/**: Contains the main API code.
- **Dockerfile**: File to contain the application.
- **pyproject.toml**: Project dependencies.
- **README.md**: Project documentation.

## Installation and Execution
### Prerequisites
- Python 3.10+
- Docker (optional, for deployment)

### Steps to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/1chavez1/MLOps-API.git
   cd project
   ```

2. Install dependencies:
It is recommended to use a virtual environment to isolate the project. If you are managing dependencies with `Poetry`, follow these steps:
Run the following command to install all dependencies defined in the `pyproject.toml` file:
  ```bash
  poetry install
```

3. Run the application:
   ```bash
   poetry run python app/run.py
   ```

4. Access the API at `http://localhost:5000`
This API has port 8080 exposed for use with Google Cloud Run, change this port to 5000 for unit testing.

### Using Docker
1. Build the Docker image:
   ```bash
   docker build -t sentiment-analysis-api .
   ```

2. Runs the container:
   ```bash
   docker run -p 5000:5000 sentiment-analysis-api
   ```

## Endpoints
### POST `/api/prediction`

#### Request
```json
{
  "review": [
    "This product is amazing! I love it."
  ]
}
```

#### Response
```json
{
  "Predicted Sentiments": [
    {"review_text": "This product is amazing! I love it.", "sentiment": "positivo"}
  ]
}
```
