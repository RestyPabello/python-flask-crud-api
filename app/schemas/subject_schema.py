from marshmallow import Schema, fields, validate, ValidationError

def non_empty_string(value):
    if not value.strip():
        raise ValidationError("Name cannot be empty or just whitespace.")

class SubjectSchema(Schema):
    name = fields.String(
        required=True, 
        validate=[non_empty_string, validate.Length(min=1, max=80)]
    )
    