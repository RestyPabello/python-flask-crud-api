from marshmallow import Schema, fields, validate, ValidationError

def non_empty_string(value):
    if not value.strip():
        raise ValidationError("Name cannot be empty or just whitespace.")

class TeacherSchema(Schema):
    name = fields.String(
        required=True, 
        validate=[non_empty_string, validate.Length(min=2, max=120)]
    )
    is_active = fields.Boolean(required=True)  
    
class TeacherListSchema(Schema):
    id         = fields.Int(dump_only=True)
    name       = fields.Str(required=True)
    is_active  = fields.Bool(required=True)
    created_at = fields.DateTime(format='%Y-%d-%m %H:%M:%S')
    updated_at = fields.DateTime(format='%Y-%d-%m %H:%M:%S')