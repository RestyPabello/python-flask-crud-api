from app.extensions import db
from datetime import datetime

class RoleType(db.Model):
    __tablename__ = 'role_types'
    
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(80), nullable=False)
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at   = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    roles = db.relationship('Role', back_populates='role_types')
    
    def __repr__(self):
        return f"<RoleType(id={self.id}, name='{self.name}')>"
