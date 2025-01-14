from marshmallow import Schema, fields, validates, ValidationError

class SubjectTeacherSchema(Schema):
    subject_id = fields.Integer(required=True, error_messages={"required": "Subject ID is required."}) 
    teacher_id = fields.Integer(required=True, error_messages={"required": "Teacher ID is required."})
    
    @validates('subject_id')
    def validate_subject_id(self, value):
        if not isinstance(value, int):
            raise ValidationError("Subject ID must be an integer.")
        
    @validates('teacher_id')
    def validate_subject_id(self, value):
        if not isinstance(value, int):
            raise ValidationError("Teacher ID must be an integer.")
        
class SubjectTeacherSchemaID(Schema):
    id = fields.Integer(
        required=True,
        error_messages={
            "required": "SubjectTeacherID is required"
        }    
    )
    is_deleted = fields.Boolean() 
        