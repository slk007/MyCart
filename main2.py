import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("mycart-python-firebase-authenticate-key.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-practise-1d48a.firebaseio.com'
})


print(db.reference('/Category').get())

