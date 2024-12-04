from flask import Blueprint, request, jsonify
from app.services.subject_service import *
from marshmallow import ValidationError
from app.schemas.subject_schema import SubjectSchema
from app.utils.helpers import handle_error

subject_bp = Blueprint("subject", __name__)

@subject_bp.route("/add-subject", methods=["POST"])
def create_subject_route():
    data   = request.json
    schema = SubjectSchema()

    try:
        validated_data = schema.load(data)
        new_subject    = add_subject(validated_data)
        
        return jsonify({
            "status_code": 201,
            "data": {
                "id": new_subject.id, 
                "name": new_subject.name
            } 
        }), 201
        
    except ValidationError as error:
        return handle_error(400, error)

    except ValueError as error:
        return handle_error(400, error)
    
@subject_bp.route("/update-subject/<int:subject_id>", methods=["PATCH"])
def update_subject_route(subject_id):
    data   = request.json
    schema = SubjectSchema()
    
    try:
        validated_data = schema.load(data)
        new_name       = validated_data.get("name")
        
        update_subject(subject_id, new_name)
        
        return jsonify({
            "status_code": 201,
            "message": "Update successful"
        }), 201
        
    except ValidationError as error:
        return handle_error(400, error)

    except ValueError as error:
        return handle_error(400, error)

    
    
    
    
    
    
    
    
    
    
    # name = data.get("name")
    
    # if not name:
    #     return jsonify({
    #         "error": "Subject name is required"
    #     }), 400
    
    # try:
    #     new_subject = add_subject(name)
    #     return jsonify({
    #         "status_code": 201,
    #         "data": {
    #             "id": new_subject.id, 
    #             "name": new_subject.name,
    #             "created_at": new_subject.created_at 
    #         } 
    #     }), 201
    # except ValueError as e:
    #     return jsonify({
    #         "status_code": 400,
    #         "error": str(e)
    #     }), 400