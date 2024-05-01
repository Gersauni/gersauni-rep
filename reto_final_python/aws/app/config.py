import os


class Config:
    # Clave secreta para la aplicación Flask
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key")

    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Test1234@database-1.c7868640g6yp.us-east-1.rds.amazonaws.com:5432/testing"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Agrega otras variables de configuración según sea necesario


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    # Agrega otras configuraciones de producción aquí


# Diccionario para mapear nombres de entorno a clases de configuración
config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    # Agrega otros entornos si es necesario
}

