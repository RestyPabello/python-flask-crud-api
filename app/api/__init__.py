# from flask import Flask
# from config import config
# from app.extensions import db
# import os  

# def create_app():
#     env = os.getenv("FLASK_ENV", "development")
#     app = Flask(__name__)
#     app.config.from_object(config[env])
#     db.init_app(app)
#     return app
