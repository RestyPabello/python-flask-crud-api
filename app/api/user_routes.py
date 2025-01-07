from flask import Blueprint, request, jsonify
from app.services.user_service import *
from marshmallow import ValidationError
from app.schemas.user_schema import *
from app.utils.helpers import handle_error
from flask_jwt_extended import create_access_token
from datetime import timedelta
from flask_jwt_extended import jwt_required

user_bp = Blueprint("user", __name__)

@user_bp.route("/get", methods=["GET"])
@jwt_required()
def get_users_route():
    try:        
        page     = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        search   = request.args.get('search', None)
        users    = get_users(page, per_page, search)
        schema   = UserListSchema(many=True)
        result   = schema.dump(users)
        
        pagination = {
            "total": users.total,
            "pages": users.pages,
            "page": users.page,
            "per_page": users.per_page,
            "has_next": users.has_next,
            "has_prev": users.has_prev
        }
        
        return jsonify({
            "status_code": 200,
            "data": result,
            "pagination": pagination
        })
        
    except ValueError as error:
        return handle_error(400, error)


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
    
@user_bp.route("/login", methods=["POST"])
def login_user_route():
    data   = request.json
    schema = LoginSchema()
    
    try:
        validated_data = schema.load(data)
        user           = login_user(validated_data)
        access_token   = create_access_token(identity=user.id, expires_delta=timedelta(days=1))
    
        return jsonify({
            "status_code": 200,
            "data": {
                "email": user.email,
                "access_token": access_token
            }
        }), 200
        
    except ValidationError as error:
        return handle_error(400, error)

    except ValueError as error:
        return handle_error(400, error)