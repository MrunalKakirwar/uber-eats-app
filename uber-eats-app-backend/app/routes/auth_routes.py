from flask import Blueprint, request, jsonify
from app.services.firebase_service import verify_firebase_token
from functools import wraps
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

auth_routes = Blueprint('auth_routes', __name__)

# Decorator to protect routes
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split("Bearer ")[-1]
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        
        try:
            # Verify the token using the Firebase service
            decoded_token = verify_firebase_token(token)
            user_id = decoded_token['uid']
            # Attach the user_id to the request context
            request.user_id = user_id
        except Exception as e:
            logging.error(f"Error verifying token: {e}")
            return jsonify({'message': 'Token is invalid or expired!'}), 403

        return f(*args, **kwargs)

    return decorated_function

# Sample protected route
@auth_routes.route('/login', methods=['POST'])
@token_required
def protected():
    return jsonify({"message": f"Welcome, user {request.user_id}!"}), 200
