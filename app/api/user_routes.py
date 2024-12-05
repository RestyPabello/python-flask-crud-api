from flask import Blueprint, request, jsonify
from app.services.user_service import *
from marshmallow import ValidationError
from app.utils.helpers import handle_error

user_bp = Blueprint("user", __name__)

@user_bp.route("/register", methods=["POST"])
def register_user_route():
    try:
        return "Hello World!"
        
    except ValidationError as error:
        return handle_error(400, error)

    except ValueError as error:
        return handle_error(400, error)