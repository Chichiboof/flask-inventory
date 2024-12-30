# Step 5: Forms
# File: app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf.file import FileField, FileAllowed

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=100)])
    author = StringField('Author', validators=[DataRequired(), Length(min=2, max=100)])
    isbn = StringField('ISBN', validators=[DataRequired(), Length(min=10, max=13)])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=0)])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)], places=2)
    description = TextAreaField('Description', validators=[Length(max=500)])
    category = SelectField('Category', coerce=int)
    cover_image = FileField('Cover Image', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
    submit = SubmitField('Save')
