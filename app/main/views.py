from fileinput import filename
from pathlib import Path
from unicodedata import name
from flask import Flask,render_template, request
import os
from config import Config
from .. import db
from .forms import ViewingForm, UploadForm
from flask import render_template,redirect,url_for
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from . import main
from ..models import House, Photo
from ..email import mail_message




@main.route('/')
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

