import os, datetime
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

from movies_library.routes import pages

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages)
    app.config["DATABASE_URL"] = os.environ.get("DATABASE_URL")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.db = MongoClient(app.config["DATABASE_URL"]).movies_library
    
    return app