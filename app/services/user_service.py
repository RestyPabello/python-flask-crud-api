from app.models.user import User
from app.extensions import db
from werkzeug.security import generate_password_hash


def register_user(validated_data):
    email            = validated_data.get('email')
    role_id          = validated_data.get('role_id')
    password         = validated_data.get('password')
    confirm_password = validated_data.get('confirm_password')
    
    hashed_password = generate_password_hash(password)
    
    new_user = User(
        email=email, 
        role_id=role_id, 
        password=hashed_password
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return new_user
    
    
