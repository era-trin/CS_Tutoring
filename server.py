from flask import Flask, render_template, request, jsonify
import pandas as pd
import json 


app = Flask(__name__, static_url_path='',static_folder = 'static')

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__': 
    app.run(debug=True, port = 8000)