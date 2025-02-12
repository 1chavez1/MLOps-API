"""
This module initializes and configures the Flask application.

It creates a Flask app instance, registers the API blueprint with a URL prefix,
prints the application's URL map (useful for debugging), and returns the configured app.
"""
from flask import Flask


def create_app():
    """
    Create and configure the Flask application instance.

    This function initializes a new Flask application, imports and registers
    the API blueprint from the 'app.api' module with the URL prefix '/api',
    and prints the URL map for debugging purposes.

    Returns:
        Flask: A Flask application instance configured with the API blueprint.
    """
    app = Flask(__name__)

    from app.api import bp
    app.register_blueprint(bp, url_prefix="/api")

    return app
