from flask import Flask, flash, redirect, render_template,request, url_for,session, abort
from flask_login import LoginManager, UserMixin,current_user,login_manager
from .. import db
from . import main
from .forms import BlogForm, CommentForm,PostForm,UserForm,UpdateForm,RegisterFrm,UploadForm
from ..models import Images, User, Blog, Comment, Post, postss, House, Photo
from flask_login import login_required
from werkzeug.utils import secure_filename
import os
from werkzeug.datastructures import  FileStorage
from fileinput import filename
from pathlib import Path
from unicodedata import name
from config import Config
from .forms import ViewingForm, UploadForm
from ..email import mail_message
from app import create_app


app=create_app('development')

#####KATE####
@main.route('/')
def index():

    return render_template("home.html")

@main.route('/contact')
def contact():

    return render_template("contact.html")


@main.route('/footer')
def footer():

    return render_template("footer.html")

#####ALBRIGHT####

@main.route('/blog/new', methods=['GET', 'POST'])

def blogs():
    """
    View Blog function that returns the Blog page and data
    """
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        title_blog= blog_form.title_blog.data
        description = blog_form.description.data
        new_blog = Blog(title_blog=title_blog, description=description)
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.blogs'))
    title = 'PrimeDale|Blog'
    return render_template('blogs.html', title=title, blog_form=blog_form)

@main.route('/blog/allblogs', methods=['GET', 'POST'])

def theblog():
    blogs = Blog.query.all()
    return render_template('myblogs.html', blogs=blogs)

#####BRIAN####

@main.route('/display')
def display():
    qr_all = postss.query.all()

    return render_template('display.html', data = qr_all)

@main.route('/update', methods = ['POST','GET'])
def update():

    dataForm =UserForm()


    if dataForm.validate_on_submit():
        addpost = postss(post = dataForm.post.data, title = dataForm.title.data)
        db.session.add(addpost)
        db.session.commit()

    
    

        return redirect(url_for('display'))
    return render_template('update.html',form = dataForm,)  



@main.route("/image",methods=["POST","GET"])
def uploadimage():
    frm=UploadForm()
    if frm.validate_on_submit():
        file=request.files["file"]
        file.save(os.path.join(app.config["UPLOAD_FOLDER"],secure_filename(file.filename)))
        upload=Images(name=secure_filename(file.filename))
        db.session.add(upload)
        db.session.commit()
        return redirect(url_for("main.viewimage"))
    return render_template("image.html",form=frm)  

@main.route("/allimages",methods=["POST","GET"])
def viewallimages():
    allimages=Images.query.all()
    return render_template("allimages.html",images=allimages)

@main.route("/viewimage",methods=["POST","GET"])
def viewimage():
    allimages=Images.query.all()
    return render_template("imageview.html",images = allimages)

    #####MAUREEN#####
@main.route('/rentals')
def rental():
    return render_template('rentals.html')

@main.route('/newrental', methods= ['GET','POST'])
def newental():

    form=UploadForm()

    if form.validate_on_submit():

        photo_path=form.file.data
        name=form.name.data
        description=form.description.data
        price=form.price.data
        photo_path.save(os.path.join(Config.UPLOADED_PHOTOS_DEST,secure_filename(photo_path.filename)))
        filename= secure_filename(photo_path.filename)
        photo_obj = Photo(photo_path=filename, name=name,description=description,price=price)
        photo_obj.save_photo()
      
        return redirect(url_for("main.rental"))

    return render_template("newrental.html",upload_form=form)


@main.route('/viewing', methods= ['GET','POST'])
def viewing():

    form=ViewingForm()

    if form.validate_on_submit():

        house=House(name=form.name.data,house=form.house.data,time=form.time.data, email=form.email.data)

        db.session.add(house)
        db.session.commit()

        mail_message("PrimeDale Realty","email/welcome", house.email)


        return redirect(url_for('main.rental'))

    return render_template('viewing.html',viewing_form=form)

    ####UNUSED####
