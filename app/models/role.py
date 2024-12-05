from app.extensions import db
from datetime import datetime

class Role(db.Model):
    __tablename__ = 'roles'
    
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(80), nullable=False)
    role_type_id = db.Column(db.Integer, db.ForeignKey('role_types.id'), nullable=False)
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at   = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    role_types = db.relationship('RoleType', back_populates='roles')
    users      = db.relationship('User', back_populates='roles')
    
    def __repr__(self):
        return f"<Role(id={self.id}, name='{self.name}')>"
