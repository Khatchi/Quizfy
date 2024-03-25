#!/usr/bin/python3
"""
This module handles the flask app as well as the corresponding routes
"""
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/home', methods=['GET', 'POST'])
def home():
    'returns home page via index.html'
    return render_template('index.html')



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)