from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField, EmailField, PasswordField,FileField
from wtforms.validators import DataRequired,Email

class BlogForm(FlaskForm):
    title_blog = StringField('Title')
    description = TextAreaField('Write a Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class PostForm(FlaskForm):
    title=StringField("Title",validators=[DataRequired()],render_kw={'placeholder':'Title'})
    post=TextAreaField("Post",render_kw={"placeholder":"Type Post..."})
    submt=SubmitField("Submit Post")


class UserForm (FlaskForm) :
    title = StringField(' Appartment',validators = [DataRequired()])
    post = StringField('Description',validators = [DataRequired()])
    
    submit = SubmitField('submit')

class UpdateForm(FlaskForm) :   
    name = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    cnfpass=PasswordField("Confirm Password",validators=[DataRequired()])
    submit = SubmitField('login')
class RegisterFrm(FlaskForm):
    name=StringField("username",validators=[DataRequired()])
    email=EmailField("Email",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    cnfpass=PasswordField("Confirm Password",validators=[DataRequired()])
    submt=SubmitField('Register')

class UploadForm(FlaskForm):
    file=FileField('Appartment',validators=[DataRequired()])
    submt=SubmitField('Upload Now')    


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
