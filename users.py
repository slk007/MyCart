from firebase import firebase
from firebase_admin import db

class Users:

    def __init__(self, name=None, email=None, password=None, admin_boolean=False):

        self.name = name
        self.email = email
        self.admin_boolean = admin_boolean

    def add_user(self, name, email="abce@gmail.com", password="", admin_boolean=False):

        data = {
            'name': name,
            'email': email,
            'password' : password,
            'admin_boolean': admin_boolean,
        }
        ref_variable = db.reference('Users').push(data)
        return ref_variable.key

    @staticmethod
    def show_users():
        users = db.reference('Users').get()
        return users

    # @staticmethod
    # def users_order_by_child():
    #     users = db.reference('Users').order_by_child('name').get()
    #     return users



# users_object = Users()
# users_object.add_user("new", "user")
