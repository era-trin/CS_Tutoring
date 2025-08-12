
from flask import Flask, render_template, request, jsonify
import pandas as pd




app = Flask(__name__, static_url_path='',static_folder = 'static')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")
if __name__ == '__main__': 
    app.run(debug=True, port = 8000)