from flask import jsonify
from marshmallow import ValidationError

def handle_error(status_code, error):
    if isinstance(error, ValidationError):
        error_message = str(error.messages)  
    elif isinstance(error, ValueError):
        error_message = str(error)

    return jsonify({
        "status_code": status_code,
        "message": error_message
    }), status_code

