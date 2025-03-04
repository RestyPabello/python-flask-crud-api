# app/__init__.py
from flask import Flask
from app.config import config
from app.extensions import init_extensions
from app.models import Teacher, Subject # * or (Subject) specific model
from app.api.subject_routes import subject_bp
from app.api.teacher_routes import teacher_bp
from app.api.user_routes import user_bp
from app.api.subject_teacher_routes import subject_teacher_bp
import os

def create_app():
    env            = os.getenv("FLASK_ENV", "development")
    jwt_secret_key = os.getenv("JWT_SECRET_KEY", "default_secret_key")

    app = Flask(__name__)
    app.config.from_object(config[env]) 
    app.config["JWT_SECRET_KEY"] = jwt_secret_key
    
    init_extensions(app)
    
    app.register_blueprint(subject_bp, url_prefix='/api/subjects')
    app.register_blueprint(teacher_bp, url_prefix='/api/teachers')
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(subject_teacher_bp, url_prefix='/api/subject-teacher')
 
    return app
