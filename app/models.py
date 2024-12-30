# Step 4: Models
# File: app/models.py

from app import db

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    books = db.relationship('Book', backref='category', lazy=True)
    
class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)  # Identifiant unique du livre
    title = db.Column(db.String(100), nullable=False)  # Titre du livre
    author = db.Column(db.String(100), nullable=False)  # Auteur du livre
    isbn = db.Column(db.String(13), unique=True)  # ISBN unique
    quantity = db.Column(db.Integer, default=0)  # Quantité disponible
    price = db.Column(db.Float, default=0.0)  # Prix du livre
    description = db.Column(db.Text)  # Description ou résumé
    added_date = db.Column(db.DateTime, default=db.func.current_timestamp())  # Date d'ajout
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)  # Clé étrangère vers Category
    cover_image = db.Column(db.String(255), nullable=True)  # Lien vers l'image de couverture

    
