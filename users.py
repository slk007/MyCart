from firebase import firebase
from firebase_admin import db

class Users:

    def __init__(self):
        self.name = None
        self.email = None
        self.password = None
        self.admin_boolean = False

    def add_user(self, name="", email="", password="", admin_boolean=False):

        data = {
            'name': name,
            'email': email,
            'password' : password,
            'admin_boolean': admin_boolean,
        }
        ref_variable = db.reference('Users').push(data)
        self.userid = ref_variable.key
        return ref_variable.key

    @staticmethod
    def get_all_users():
        users = db.reference('Users').get()
        return users

    @staticmethod
    def get_user_by_id(id):
        user = db.reference("Users/{}".format(id)).get()
        return user

    @staticmethod
    def add_to_cart(userid, product):
        db.reference("Users/{}/cart".format(userid)).push(product)
        print("Added to Cart")

    @staticmethod
    def view_cart(user_id):
        print("-"*13, "CART", "-"*13)
        cart_dict = db.reference("Users/{}/cart".format(user_id)).get()
        print("-"*30)
        for key,values in cart_dict.items():
            print(values['Name'], ", Rs.", values['Price'])
        print("-"*30)

    @staticmethod
    def generate_bill(user_id):
        cart_dict = db.reference("Users/{}/cart".format(user_id)).get()
        actual_amount = 0
        for key,values in cart_dict.items():
            actual_amount += int(values['Price'])
        return actual_amount

    @staticmethod
    def remove__product_from_cart(product):
        pass

