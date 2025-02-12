"""
This module serves as the entry point for the Flask application.

It creates the Flask application instance using the factory function `create_app()`
from the `app` module and runs the development server when executed directly.
"""


from app.api import bp
from app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
