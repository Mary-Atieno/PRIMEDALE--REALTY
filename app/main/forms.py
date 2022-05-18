from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class BlogForm(FlaskForm):
    title_blog = StringField('Title')
    description = TextAreaField('Write a Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment', validators=[DataRequired()])
    submit = SubmitField('Comment')
