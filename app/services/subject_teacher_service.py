from app.models import SubjectTeacher, Subject, Teacher
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from app.extensions import db

def add_subject_teacher(validated_data):
    subject_id = int(validated_data.get("subject_id"))
    teacher_id = int(validated_data.get("teacher_id"))
    
    new_subject_teacher = SubjectTeacher(subject_id=subject_id, teacher_id=teacher_id)
    
    db.session.add(new_subject_teacher)
    db.session.commit()
    
    return new_subject_teacher.to_dict()

def get_subjects_teachers(page, per_page, search=None):
    subject_teacher_query = SubjectTeacher.query.options(
        joinedload(SubjectTeacher.subjects),
        joinedload(SubjectTeacher.teachers)
    )
    
    if search:
        subject_teacher_query = subject_teacher_query.join(
                SubjectTeacher.subjects
            ).join(
                SubjectTeacher.teachers
            ).filter(
            or_(Subject.name.ilike(f"%{search}%"), 
                Teacher.name.ilike(f"%{search}%") 
            )
        )
        
    subject_teachers = subject_teacher_query.paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    result = []
    for st in subject_teachers.items:
        result.append({
            "id": st.id,
            "subject_name": st.subjects.name,
            "teacher_name": st.teachers.name,
            "is_active": st.teachers.is_active
        })
        
    pagination = {
        "total": subject_teachers.total,
        "pages": subject_teachers.pages,
        "page": subject_teachers.page,
        "per_page": subject_teachers.per_page,
        "has_next": subject_teachers.has_next,
        "has_prev": subject_teachers.has_prev
    }

    return {
        "result": result,
        "pagination": pagination
    }
    
