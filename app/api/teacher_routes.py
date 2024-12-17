from flask import Blueprint, request, jsonify
from app.services.teacher_service import *
from marshmallow import ValidationError
from app.schemas.teacher_schema import *
from app.utils.helpers import handle_error
# from flask_jwt_extended import jwt_required

teacher_bp = Blueprint("teacher", __name__)

@teacher_bp.route("/get", methods=["GET"])
# @jwt_required()
def get_teachers_route():
    try:        
        page     = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        search   = request.args.get('search', None)
        teachers = get_teachers(page, per_page, search)
        schema   = TeacherListSchema(many=True)
        result   = schema.dump(teachers)
        
        pagination = {
            "total": teachers.total,
            "pages": teachers.pages,
            "page": teachers.page,
            "per_page": teachers.per_page,
            "has_next": teachers.has_next,
            "has_prev": teachers.has_prev
        }
        
        return jsonify({
            "status_code": 200,
            "data": result,
            "pagination": pagination
        })
        
    except ValueError as error:
        return handle_error(400, error)
    

@teacher_bp.route("/add-teacher", methods=["POST"])
def create_teacher_route():
    data   = request.json
    schema = TeacherSchema()
    
    try:
        validated_data = schema.load(data)    
        new_teacher    = add_teacher(validated_data)
        
        return jsonify({    
            "status_code": 200,
            "data": {
                "id": new_teacher.id, 
                "name": new_teacher.name,
                "is_active": new_teacher.is_active
            } 
        }), 200
         
    except ValidationError as error:
        return handle_error(400, error)

    except ValueError as error:
        return handle_error(400, error)
    
@teacher_bp.route("/update-teacher/<int:teacher_id>", methods=["PUT"])
def update_teacher_route(teacher_id):
    data   = request.json
    schema = TeacherSchema()
    
    try:
        validated_data = schema.load(data)
        new_name       = validated_data.get("name")
        is_active      = validated_data.get("is_active")
        
        update_teacher(teacher_id, new_name, is_active)
        
        return jsonify({
            "status_code": 200,
            "message": "Update successful"
        }), 200
        
    except ValidationError as error:
        return handle_error(400, error)

    except ValueError as error:
        return handle_error(400, error)