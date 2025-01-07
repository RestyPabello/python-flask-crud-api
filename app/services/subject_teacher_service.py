from app.models.subject_teacher import SubjectTeacher
from app.extensions import db

def add_subject_teacher(validated_data):
    subject_id = int(validated_data.get("subject_id"))
    teacher_id = int(validated_data.get("teacher_id"))
    
    new_subject_teacher = SubjectTeacher(subject_id=subject_id, teacher_id=teacher_id)
    
    db.session.add(new_subject_teacher)
    db.session.commit()
    
    return new_subject_teacher.to_dict()
    
