from flask import Flask, request
from dotenv import load_dotenv
from .routes import main

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.register_blueprint(main)

    return app