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
    
@subject_teacher_bp.route("/get", methods=["GET"])
@jwt_required()
def get_subjects_teachers_route():
    try:  
        page     = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        search   = request.args.get('search', None)
        
        subjects_teachers = get_subjects_teachers(page, per_page, search)
        
        return jsonify({
            "status_code": 200,
            "data": subjects_teachers["result"],  
            "pagination": subjects_teachers["pagination"]
        })
        
    except ValueError as error:
        return handle_error(400, error)
    
@subject_teacher_bp.route("/update/<int:id>", methods=["PUT"])
@jwt_required()
def update_subject_teacher_route(id):
    data       = request.json
    data["id"] = id
    
    schema = SubjectTeacherSchemaID()

    try:
        validated_data = schema.load(data)
        is_deleted     = validated_data.get("is_deleted")
        
        update_subject_teacher(id, is_deleted)
        
        return jsonify({
            "status_code": 200,
            "message": "Update successful"
        }), 200
    
    except ValidationError as error:
        return handle_error(400, error)

    except ValueError as error:
        return handle_error(400, error)
    
    