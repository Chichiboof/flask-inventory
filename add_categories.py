from app import create_app, db
from app.models import Category

# Créer l'application Flask
app = create_app()

# Liste des catégories à ajouter
categories = [
    {"name": "Classic", "description": "Classic literature"},
    {"name": "Fiction", "description": "Books based on fictional stories"},
    {"name": "Science Fiction", "description": "Books with futuristic themes and technologies"},
    {"name": "Fantasy", "description": "Books with magical and mythical elements"},
    {"name": "Mystery", "description": "Books focusing on solving crimes or mysteries"},
    {"name": "Biography", "description": "Books about real people's lives"},
    {"name": "History", "description": "Books based on historical events"},
    {"name": "Philosophy", "description": "Books exploring philosophical concepts"},
    {"name": "Romance", "description": "Books focused on romantic relationships"},
    {"name": "Non-Fiction", "description": "Books based on real events or factual information"}
]

# Contexte de l'application pour insérer les données
with app.app_context():
    # Récupérer dynamiquement le nom de la table associée au modèle `Category`
    category_table_name = Category.__tablename__
    print(f"Inserting data into table: {category_table_name}")

    for cat in categories:
        # Vérifier si la catégorie existe déjà
        existing_category = Category.query.filter_by(name=cat["name"]).first()
        if not existing_category:
            new_category = Category(name=cat["name"], description=cat["description"])
            db.session.add(new_category)
            print(f"Added category: {cat['name']}")
        else:
            print(f"Category '{cat['name']}' already exists, skipping.")

    # Commit des modifications
    db.session.commit()
    print("All categories have been added to the database.")
    print(f"Database path: {db.engine.url}")