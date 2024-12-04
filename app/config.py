from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY                     = os.getenv("SECRET_KEY", "default_secret_key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG                          = False
    SQLALCHEMY_DATABASE_URI        = os.getenv("DATABASE_URL")

    
class DevelopmentConfig(Config):
    DEBUG = True
    
config = {
    'development': DevelopmentConfig
}