from app.models.subject import Subject
from app.extensions import db 

def add_subject(validated_data):
    name             = validated_data.get("name")
    existing_subject = Subject.query.filter_by(name=name).first()

    if existing_subject:
        raise ValueError("Subject already exists")
    
    new_subject = Subject(name=name)
    
    db.session.add(new_subject)
    db.session.commit()
    
    return new_subject  

def update_subject(subject_id, new_name=None):
    subject = Subject.query.get(subject_id)
    
    if not subject:
        raise ValueError("Subject is not found")
    
    existing_subject = Subject.query.filter(
        Subject.name == new_name, Subject.id != subject_id
    ).first()
    
    if existing_subject:
        raise ValueError("Subject already exists")
    
    if new_name is not None:
        subject.name = new_name
    
    db.session.commit()
    
    
