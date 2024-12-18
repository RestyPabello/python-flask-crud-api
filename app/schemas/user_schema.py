from marshmallow import Schema, fields, validate, ValidationError, validates_schema, validates
from app.models.user import User

def non_empty_string(value):
    if not value.strip():
        raise ValidationError("Name cannot be empty or just whitespace.")
    
def validate_password(password):
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must contain at least one number.")
    if not any(char.isalpha() for char in password):
        raise ValidationError("Password must contain at least one letter.")
    if not any(char in "!@#$%^&*()-_+=" for char in password):
        raise ValidationError("Password must contain at least one special character.")

class UserSchema(Schema):
    email = fields.Email(
        required=True, 
        error_messages={
            "required": "Email is required.", 
            "invalid": "Invalid email address."
        }
    )
    role_id = fields.Integer(required=True)
    password = fields.String(
        required=True,
        validate=[validate_password, validate.Length(max=128)],
        error_messages={
            "required": "Password is required."
        }
    )
    confirm_password = fields.String(
        required=True,
        error_messages={"required": "Password confirmation is required."}
    )
    
    @validates("email")
    def validate_email_exists(self, value):
        if User.query.filter_by(email=value).first():
            raise ValidationError("Email already exists")

    @validates_schema
    def validate_passwords_match(self, data, **kwargs):
        if data.get('password') != data.get('confirm_password'):
            raise ValidationError({"confirm_password": "Passwords do not match."})
        
class LoginSchema(Schema):
    email = fields.Email(
        required=True, 
        error_messages={
            "required": "Email is required.", 
            "invalid": "Invalid email format."
        }
    )
    password = fields.String(
        required=True,
        error_messages={
            "required": "Password is required."
        }
    )