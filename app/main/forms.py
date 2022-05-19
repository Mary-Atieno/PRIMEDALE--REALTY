from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, FileField
from wtforms.validators import DataRequired,Email

class ViewingForm(FlaskForm):
    email=StringField('Your Email',validators=[DataRequired()])
    name=StringField('Your Name',validators=[DataRequired()])
    house=StringField('Specify House Name',validators=[DataRequired()])
    time=TextAreaField('Enter Month and Day Preffered ',validators = [DataRequired()])
    submit = SubmitField('Post')

class UploadForm(FlaskForm):
    file=FileField('Add a File',validators=[DataRequired()])
    name = StringField('Enter house name',validators=[DataRequired()])
    description = StringField('Describe your listing',validators=[DataRequired()])
    price = StringField('Give price in dollars',validators=[DataRequired()])
    submt=SubmitField('Upload')