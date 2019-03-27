import os
from os import environ

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
  """Base configuration."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = environ.get("JWT_SECRET_KEY")
    JSON_SORT_KEYS = False


class DevelopmentConfig(BaseConfig):
   """Development configuration."""
    DEBUG = True
    TESTING = False
    ENV = "Development"


class TestingConfig(BaseConfig):
   """Testing configuration."""
    DEBUG = True
    TESTING = True
    ENV = "Testing"


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
    TESTING = False
    ENV = "Production"


app_config = {
    "Development": DevelopmentConfig,
    "Testing": TestingConfig,
    "Production": ProductionConfig
}
