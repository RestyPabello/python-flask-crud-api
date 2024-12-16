from flask import Blueprint, request, jsonify
from app.services.user_service import *
from marshmallow import ValidationError
from app.schemas.user_schema import *
from app.utils.helpers import handle_error

user_bp = Blueprint("user", __name__)

@user_bp.route("/register", methods=["POST"])
def register_user_route():
    data   = request.json
    schema = UserSchema()
    
    try:
        validated_data = schema.load(data)
        new_user = register_user(validated_data)
        
        return jsonify({
            "status_code": 200,
            "data": {
                "id": new_user.id,
                "role_id": new_user.role_id,
                "email": new_user.email
            }
        }), 200
        
    except ValidationError as error:
        return handle_error(400, error)

    except ValueError as error:
        return handle_error(400, error)