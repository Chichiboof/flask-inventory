# File: app/routes.py


from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from werkzeug.utils import secure_filename
from app.forms import BookForm
from app.models import Book, Category, db
import os

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    books = Book.query.all()
    return render_template('home.html', books=books)


@bp.route('/books', methods=['GET'])
def list_books():
    books = Book.query.all()  # Récupère tous les livres
    return render_template('list_books.html', books=books)

@bp.route('/book/add', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    form.category.choices = [(c.id, c.name) for c in Category.query.all()]

    if form.validate_on_submit():
        # Gérer le téléchargement de l'image
        cover_image_path = None
        if form.cover_image.data:
            filename = secure_filename(form.cover_image.data.filename)
            cover_image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            form.cover_image.data.save(cover_image_path)

            # Convertir le chemin en relatif pour l'utiliser dans l'application
            cover_image_path = f'static/uploads/{filename}'

        # Ajouter le livre dans la base de données
        book = Book(
            title=form.title.data,
            author=form.author.data,
            isbn=form.isbn.data,
            quantity=form.quantity.data,
            price=form.price.data,
            description=form.description.data,
            category_id=form.category.data,
            cover_image=cover_image_path
        )
        db.session.add(book)
        db.session.commit()
        flash('Book added successfully!', 'success')
        return redirect(url_for('routes.list_books'))

    return render_template('book_form.html', form=form)


@bp.route('/book/update/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    # Récupérer le livre à partir de son ID
    book = Book.query.get_or_404(book_id)
    form = BookForm()

    # Charger les catégories dans le SelectField
    form.category.choices = [(c.id, c.name) for c in Category.query.all()]

    # Pré-remplir le formulaire avec les données actuelles
    if request.method == 'GET':
        form.title.data = book.title
        form.author.data = book.author
        form.isbn.data = book.isbn
        form.quantity.data = book.quantity
        form.price.data = book.price
        form.description.data = book.description
        form.category.data = book.category_id

    if form.validate_on_submit():
        # Mettre à jour les champs avec les nouvelles données
        book.title = form.title.data
        book.author = form.author.data
        book.isbn = form.isbn.data
        book.quantity = form.quantity.data
        book.price = form.price.data
        book.description = form.description.data
        book.category_id = form.category.data

        # Gérer la mise à jour de l'image si une nouvelle image est sélectionnée
        if form.cover_image.data:
            filename = secure_filename(form.cover_image.data.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            form.cover_image.data.save(filepath)
            book.cover_image = f'static/uploads/{filename}'

        # Sauvegarder les modifications dans la base de données
        db.session.commit()
        flash('Book updated successfully!', 'success')
        return redirect(url_for('routes.list_books'))

    return render_template('book_form.html', form=form, title="Update Book")
