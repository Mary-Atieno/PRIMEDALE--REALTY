
from flask import Flask, render_template


app = Flask(__name__, template_folder='Templates',
            static_folder='static', static_url_path="/static")


@app.route('/')
def index():

    return render_template("home.html")


@app.route('/contact')
def contact():

    return render_template("contact.html")


@app.route('/footer')
def footer():

    return render_template("footer.html")





if __name__ == "__main__":
    app.run(debug=True)
