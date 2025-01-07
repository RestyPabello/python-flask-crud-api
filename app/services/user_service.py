from app.models.user import User
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


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

def login_user(validated_data):
    email    = validated_data.get('email')
    password = validated_data.get('password')
    
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        raise ValueError("Invalid email or password")
     
    return user

def get_users(page=1, per_page=10, search=None):
    user_query = User.query
    
    if search:
        user_query = user_query.filter(
            (User.name.ilike(f"%{search}%"))
        )
        
    users = user_query.order_by(User.id).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return users

    
