"""
This module sets up the ML model configuartion.

It utilizes Pydantic's BaseSettings for configuartion managment,
allowing settings to be read from enviroment variables and a .env file.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelSettings(BaseSettings):
    """
    ML model configuartion settings for the application.

    Attributes:
        model_config (SettingsConfigDict): Model config, loaded from .env file.
        model_path (str): Name of the ML model path.
        model_name: (str): Name of the ML model.
        vectorizer: (str): Name of the vectorizer.
    """

    model_config = SettingsConfigDict(
        env_file='app/config/.env',
        env_file_encoding='utf-8',
        protected_namespaces=('settings_',),
        extra='ignore',
    )

    model_path: str
    model_name: str
    vectorizer: str


model_settings = ModelSettings()
