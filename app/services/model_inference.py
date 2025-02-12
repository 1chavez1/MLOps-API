"""
This module provides functionality for making predictions.

It contains the ModelInferenceService class, which offers methods to load
a model from a file, and to make perdictions using the lodaded model.
"""

from pathlib import Path

import joblib
from loguru import logger
import torch

from app.config import model_settings


class ModelInferenceService:
    """A service class for making predictions.

    This class provides functionalities to load a ML model from
    a specified path, and make predictions using the loaded model.

    Attributes:
        model: ML model managed by this service. Initially set to None.
        model_path: Directory to extract the model from.
        model_name: Name of the saved model to use.
        vectorizer: Name of the saved vectorizer to use.

    Methods:
        __init__: Constructor that initializes the ModelInferenceService.
        load_model: Loads the model from file.
        predict: Makes a prediction using the loaded model.
    """

    def __init__(self) -> None:
        """Initialize the ModelService with no model loaded."""
        self.model = None
        self.model_path = model_settings.model_path
        self.model_name = model_settings.model_name
        self.vectorizer = model_settings.vectorizer

    def load_model(self) -> None:
        """
        Load the model from a specified path.

        Raises:
            FileNotFoundError: If the model file not exist at specified dir.
        """
        logger.info(
            'Checking the existance of model config file at '
            f'{self.model_path}/{self.model_name}',
        )
        model_path = Path(self.model_path) / self.model_name

        if not model_path.exists():
            raise FileNotFoundError('Model file does not exist.')

        logger.info(
            f'model{self.model_name} exists! ->',
            'loading model configuration file',
        )

        with open(model_path, 'rb') as model_file:
            self.model = torch.jit.load(model_file)

    def predict(self, reviews: list[str]) -> list[dict]:
        """
        Make a prediction using the loaded model.

        Takes input parameters and passes it to the model, which
        was loaded using a torch file.

        Args:
            input_params (list): The input data for making a prediction.

        Returns:
            list: The prediction result from the model.
        """
        logger.info('Making prediction')
        self.model.eval()

        model_path = Path(self.model_path) / self.vectorizer
        vectorizer = joblib.load(model_path)
        new_data_transformed = vectorizer.transform(reviews).toarray()
        new_data_tensor = torch.tensor(new_data_transformed, dtype=torch.float32)

        with torch.no_grad():
            predictions = self.model(new_data_tensor)
            _, predicted_classes = torch.max(predictions, 1)

        sentiment_labels = {0: "negativo", 1: "neutral", 2: "positivo"}
        predicted_labels = [sentiment_labels[class_idx] for class_idx in predicted_classes.cpu().numpy()]

        result = [
            {"review_text": review, "sentiment": sentiment}
            for review, sentiment in zip(reviews, predicted_labels)
        ]
        return result
