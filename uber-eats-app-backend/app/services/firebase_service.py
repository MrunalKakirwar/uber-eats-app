import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin.exceptions import FirebaseError

# Initialize Firebase Admin SDK with service account credentials
def initialize_firebase():
    try:
        cred = credentials.Certificate("/Users/csuftitan/Downloads/cred.json")
        firebase_admin.initialize_app(cred)
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        raise e

# Function to verify the Firebase ID token
def verify_firebase_token(token):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except auth.ExpiredIdTokenError:
        raise Exception("Token expired")
    except auth.InvalidIdTokenError:
        raise Exception("Token is invalid")
    except Exception as e:
        raise Exception(f"Error verifying token: {str(e)}")
