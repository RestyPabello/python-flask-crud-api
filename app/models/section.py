from app.extensions import db
from datetime import datetime

class Section(db.Model):
    __tablename__ = 'sections'
    
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    students = db.relationship('Student', back_populates='section')

    def __repr__(self):
        return f"<Section(id={self.id}, name='{self.name}')>"
