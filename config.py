# Step 3: Configuration File
# File: config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app/static/uploads')  # Chemin pour stocker les images
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # Limite de 2 Mo pour les fichiers uploadés
