
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth

def certify():
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate("mycart-python-firebase-authenticate-key.json")

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
    'data': "https://mycart-python.firebaseio.com/"
    })
    # As an admin, the app has access to read and write all data, regradless of Security Rules


# certify()
# add_product()
