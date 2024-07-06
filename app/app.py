#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

authdb = SQLAlchemy(app)

from .models import User, Organization

def innit_db():
    authdb.create_all()

if __name__ == "__main__":
    app.run(debug=True)
