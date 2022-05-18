
from flask import Flask, render_template

app = Flask(__name__ ,template_folder= 'Templates', static_folder='static',static_url_path="/static")

@app.route('/')
def index():

    return render_template("navbar.html")

@app.route('/contact')
def home():

    return render_template("contact.html")


if __name__ == "__main__":
    app.run( debug = True )