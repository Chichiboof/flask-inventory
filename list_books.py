from app import create_app, db
from app.models import Book

# Créer l'application Flask
app = create_app()

# Contexte de l'application pour interroger la base de données
with app.app_context():
    # Récupérer toutes les catégories
    books = Book.query.all()

    # Afficher chaque catégorie
    if books:
        print("List of Books:")
        for book in books:
            print(f"ID: {book.id}, Name: {book.title}, Description: {book.description}")
    else:
        print("No book found in the table 'book'.")
