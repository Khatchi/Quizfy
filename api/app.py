#!/usr/bin/python3
"""
This module handles the flask app as well as the corresponding routes
"""
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Question, Options, Quiz
from dotenv import load_dotenv
import os
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import check_password_hash, Bcrypt, generate_password_hash
import requests
import json


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
bcrypt = Bcrypt()

db.init_app(app)


@app.route('/home', methods=['GET', 'POST'])
def home():
    'returns home page via index.html'
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    "returns and stores new user"
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Checks if the username is already taken
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already taken. Please choose another.', 'danger')
            return redirect(url_for('register'))

        # Hashes the password before storing it in the database
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Creates a new user instance
        new_user = User(email=email, password=hashed_password)

        # Commits the user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully. You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    'returns the login template'
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    'returns user to the home page'
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    'returns the dashboard template'
    quizzes = Quiz.query.all()
    return render_template('dashboard.html', quizzes=quizzes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)