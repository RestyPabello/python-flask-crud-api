from app.extensions import db
from datetime import datetime

class Teacher(db.Model):
    __tablename__ = 'teachers'
    
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(80), nullable=False)
    is_active  = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    subject_teachers = db.relationship('SubjectTeacher', back_populates='teachers')
    
    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}', is_active={self.is_active})>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
