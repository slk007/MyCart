from firebase import firebase
from firebase_admin import db

class Users:

    def __init__(self, firstname=None, lastname=None, email=None, admin_boolean=False):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.admin_boolean = admin_boolean

    def add_user(self, firstname, lastname, email="abce@gmail.com", admin_boolean=False):

        data = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'admin_boolean': admin_boolean
        }
        ref_variable = db.reference('Users').set()
        print(ref_variable.key)

    @staticmethod
    def show_users():
        users = db.reference('Users').get()
        return users
        

# users_object = Users()
# users_object.add_user("new", "user")
