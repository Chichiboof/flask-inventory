from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()
    print("Tables created successfully.")
    
 # Debug : Afficher les tables existantes
    inspector = db.inspect(db.engine)
    print("Tables in the database:", inspector.get_table_names())
    
    print(f"Database path: {db.engine.url}")
    db.create_all()
