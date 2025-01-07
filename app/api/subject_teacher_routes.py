from flask import Blueprint, request, jsonify
from app.services.subject_teacher_service import *
from marshmallow import ValidationError
from app.schemas.subject_teacher_schema import *
from app.utils.helpers import handle_error
from flask_jwt_extended import jwt_required

subject_teacher_bp = Blueprint("subject_teacher", __name__)

@subject_teacher_bp.route("/add", methods=["POST"])
@jwt_required()
def create_subject_teacher_route():
    data   = request.json
    schema = SubjectTeacherSchema()
    
    try:        
        validated_data = schema.load(data)
        
        add_subject_teacher(validated_data)
        
        return jsonify({
            "status_code": 200,
            "message": "Created successfully"
        })
        
    except ValidationError as error:
        return handle_error(400, error)
        
    except ValueError as error:
        return handle_error(400, error)