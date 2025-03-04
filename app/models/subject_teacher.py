from app.extensions import db
from datetime import datetime

class SubjectTeacher(db.Model):
    __tablename__ = 'subject_teachers'
    
    id         = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)
    
    subjects = db.relationship('Subject', back_populates='subject_teachers')
    teachers = db.relationship('Teacher', back_populates='subject_teachers') 
    
    def __repr__(self):
        return f"<SubjectTeacher(subject_id={self.subject_id}, teacher_id={self.teacher_id})>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "subject_id": self.subject_id,
            "teacher_id": self.teacher_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
