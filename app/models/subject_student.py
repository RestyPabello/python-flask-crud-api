from app.extensions import db
from datetime import datetime

class SubjectStudent(db.Model):
    __tablename__ = 'subject_students'
    
    id         = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    subjects = db.relationship('Subject', back_populates='subject_students')
    students = db.relationship('Student', back_populates='subject_students')
    
    def __repr__(self):
        return f"<SubjectStudent(subject_id={self.subject_id}, student_id={self.student_id})>"
