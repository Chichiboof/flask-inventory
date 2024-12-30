from app import create_app, db
from app.models import Book, Category

# Créer l'application Flask
app = create_app()

# Liste des données à insérer
books = [
    {
        "title": "1984",
        "author": "George Orwell",
        "isbn": "9780451524935",
        "quantity": 10,
        "price": 15.99,
        "description": "A dystopian novel about a totalitarian regime.",
        "category_id": 1,
        "cover_image": "https://example.com/covers/1984.jpg"
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "isbn": "9780061120084",
        "quantity": 5,
        "price": 18.99,
        "description": "A story of justice and moral growth.",
        "category_id": 2,
        "cover_image": "https://example.com/covers/mock.jpg"
    }
]

# Contexte de l'application pour insérer les données
with app.app_context():
    for book_data in books:
        book = Book(**book_data)
        db.session.add(book)

    # Commit des modifications
    db.session.commit()
    print("Books added successfully!")
