from app import create_app, db
from app.models import Category

# Créer l'application Flask
app = create_app()

# Contexte de l'application pour interroger la base de données
with app.app_context():
    # Récupérer toutes les catégories
    categories = Category.query.all()

    # Afficher chaque catégorie
    if categories:
        print("List of Categories:")
        for category in categories:
            print(f"ID: {category.id}, Name: {category.name}, Description: {category.description}")
    else:
        print("No categories found in the table 'category'.")
