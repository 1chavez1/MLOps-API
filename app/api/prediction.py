"""
Prediction API module.

This module contains endpoints to trigger a machine learning model
for predicting sentiment analysis on reviews of customers.

Endpoints:

    - POST /api/prediction:
        Returns a prediction for sentiment analysis based on the JSON data
        provided in the request body. The request body should contain JSON
        data that matches the schema defined in the Analysis class.
        Returns HTTP status 400 if the input paramters are invalid.
"""

from flask import Blueprint, request

from app.schema import Analysis
from app.services import model_inference_service


bp = Blueprint('prediction', __name__)


@bp.post('/prediction')
def get_prediction_post():
    """
    Returns a prediction based on the Json data provided.

        Returns:
            prediction: JSON
    """
    try:
        data = request.get_json()
        if not data:
            return {'error': 'No JSON data provided'}, 400
        review_features = Analysis(**data)
        prediction = model_inference_service.predict(review_features.review)
        return {'Predicted Sentiments': prediction}, 200
    except Exception as e:
        return {'Bad inputs data': str(e)}, 400
