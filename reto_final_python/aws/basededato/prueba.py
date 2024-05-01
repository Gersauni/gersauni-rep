from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Configuración de la base de datos
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = "sqlite:///" + os.path.join(basedir, "database.db")

# Inicialización de la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la extensión SQLAlchemy
db = SQLAlchemy(app)

# Definición de tu modelo de datos aquí

if __name__ == "__main__":
    with app.app_context():
        # Crea todas las tablas definidas en los modelos
        db.create_all()
