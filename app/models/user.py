from app.extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id         = db.Column(db.Integer, primary_key=True)
    email      = db.Column(db.String(320), unique=True, nullable=False) 
    password   = db.Column(db.String(128), nullable=False)
    role_id    = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    roles = db.relationship('Role', back_populates='roles')
    
    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"