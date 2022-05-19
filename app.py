from crypt import methods
# from quote import app 

from email.mime import image

from flask_login import LoginManager, UserMixin,current_user,login_manager

from flask import Flask, redirect, render_template, request,flash, session, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, PasswordField
from wtforms.validators import DataRequired
# from flask_migrate import Migrate

from wtforms import StringField,SubmitField,PasswordField,FileField,TextAreaField,EmailField
from wtforms.validators import DataRequired

import os















  
from signal import valid_signals
from flask import Flask, flash, redirect, render_template,request, url_for,session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,FileField,TextAreaField,EmailField
from wtforms.validators import DataRequired

from werkzeug.utils import secure_filename





app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SECRET_KEY']='my secrecte key'


app.config["UPLOAD_FOLDER"]="static/uploads"
app.config["MAIL_DEFAULT_SENDER"]="brian108otieno@gmail.com"
app.config["MAIL_USERNAME"]="brian108otieno@gmail.com"
app.config["MAIL_PORT"]= 465
app.config["MAIL_SERVER"]='smtp.gmail.com', 465
app.config["MAIL_USE_TLS"]=True
app.config["MAIL_USE_SSL"]=True
app.config['MAIL_USERNAME']=os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD']=os.environ.get('EMAIL_PASS')






db = SQLAlchemy(app)
login_manager = LoginManager(app)






class posts(db.Model):
    id = db.Column(db.String, primary_key = True)
    blogs = db.Column(db.String(50) , primary_key = False)
    post = db.Column(db.String(50), primary_key = False)



class postss(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(25),nullable =False) 
    post = db.Column(db.String(50),nullable =False)
    poster=db.Column(db.Integer,db.ForeignKey('user.id'))
    # poster=db.Column(db.Integer,db.ForeignKey('user.id'))
 
 
#user Model
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(40),nullable=False)
    email=db.Column(db.String(40),nullable=False)
    password=db.Column(db.String(40),nullable=False)
    postman=db.relationship('Post',backref="postman")


class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    post=db.Column(db.String(700),nullable=False)
    poster=db.Column(db.Integer,db.ForeignKey('user.id'))

class Images(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    uploader_id=db.Column(db.Integer,db.ForeignKey('user.id'))





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



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))









@app.route('/display')
def display():
    qr_all = postss.query.all()

    return render_template('display.html', data = qr_all)





@app.route('/', methods = ['POST','GET'])
def index():

    dataForm =UserForm()


    if dataForm.validate_on_submit():
        addpost = postss(post = dataForm.post.data, title = dataForm.title.data)
        db.session.add(addpost)
        db.session.commit()

    
    

        return redirect(url_for('display'))
    return render_template('update.html',form = dataForm,)  



@app.route("/image",methods=["POST","GET"])
def uploadimage():
    frm=UploadForm()
    if frm.validate_on_submit():
        file=request.files["file"]
        file.save(os.path.join(app.config["UPLOAD_FOLDER"],secure_filename(file.filename)))
        upload=Images(name=secure_filename(file.filename))
        db.session.add(upload)
        db.session.commit()
        return redirect(url_for("viewimage"))
    return render_template("image.html",form=frm)




    

@app.route("/allimages",methods=["POST","GET"])
def viewallimages():
    allimages=Images.query.all()
    return render_template("allimages.html",images=allimages)

@app.route("/viewimage",methods=["POST","GET"])
def viewimage():
    allimages=Images.query.all()
    return render_template("imageview.html",images = allimages)










if __name__=='__main__':
    app.run(debug=1)



