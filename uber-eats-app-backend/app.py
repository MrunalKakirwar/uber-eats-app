from flask import Flask
from app.routes.auth_routes import auth_routes
from app.services.firebase_service import initialize_firebase
from app import create_app

app = create_app()

# Initialize Firebase
initialize_firebase()

if __name__ == "__main__":
    app.run(debug=True)
