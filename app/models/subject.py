from app.extensions import db
from datetime import datetime

class Subject(db.Model):
    __tablename__ = 'subjects'
    
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Use string reference to avoid circular import issues
    subject_students = db.relationship('SubjectStudent', back_populates='subjects')
    subject_teachers = db.relationship('SubjectTeacher', back_populates='subjects')

    def __repr__(self):
        return f"<Subject(id={self.id}, name='{self.name}')>"
