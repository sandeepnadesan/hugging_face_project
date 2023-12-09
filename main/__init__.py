# from flask import Flask
from flask import Flask, render_template


app = Flask(__name__,template_folder="templete")


# Route to render the HTML page
@app.route('/')
def index():
    return render_template('home.html')

from main.api import route