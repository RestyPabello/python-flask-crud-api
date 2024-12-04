from app.extensions import db
from datetime import datetime

class Student(db.Model):
    __tablename__ = 'students'
    
    id         = db.Column(db.Integer, primary_key=True)
    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'), nullable=False)
    name       = db.Column(db.String(80), nullable=False)
    is_active  = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    section          = db.relationship('Section', back_populates='students')
    subject_students = db.relationship('SubjectStudent', back_populates='students')
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', is_active={self.is_active})>"
