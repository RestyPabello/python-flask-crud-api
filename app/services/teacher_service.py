from app.models.teacher import Teacher
from app.extensions import db

def get_teachers(page=1, per_page=10, search=None):
    teacher_query = Teacher.query
    
    if search:
        teacher_query = teacher_query.filter(
            (Teacher.name.ilike(f"%{search}%"))
        )
        
    teachers = teacher_query.order_by(Teacher.id).paginate(
        page=page, per_page=per_page, error_out=False
    )

    return teachers

def add_teacher(validated_data):
    name      = validated_data.get("name")
    is_active = validated_data.get("is_active", True)
    
    new_teacher = Teacher(name=name, is_active=is_active)
    
    db.session.add(new_teacher)
    db.session.commit()
    
    return new_teacher

def update_teacher(teacher_id, new_name=None, is_active=None):
    teacher = Teacher.query.get(teacher_id)
    
    if not teacher:
        raise ValueError("Teacher is not found")
    
    if new_name is not None:
        teacher.name = new_name
    if is_active is not None:
        teacher.is_active = is_active
    
    teacher.name      = new_name
    teacher.is_active = is_active
    
    db.session.commit()