from firebase import firebase
from firebase_admin import db

from prettytable import PrettyTable

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
    def get_user_id_by_user_name(username):
        user_dic = db.reference("Users").order_by_child("name").equal_to(username).get()
        user_id = ""    
        for key,value in user_dic.items():
            user_id = key
        return user_id

    @staticmethod
    def add_to_cart(userid, product):
        db.reference("Users/{}/cart".format(userid)).push(product)
        print("Added to Cart")

    @staticmethod
    def view_cart(user_id):
        print("-"*13, "CART", "-"*13)
        cart_dict = db.reference("Users/{}/cart".format(user_id)).get()

        flag = False

        t = PrettyTable(["Cart Item", "Price"])
        if cart_dict:
            flag=True
            for key,values in cart_dict.items():
                t.add_row([values['Name'], values['Price']])
        else:
            flag=False
            t.add_row(["No Item", "Empty"])
        print(t)
        print("-"*30)
        return flag

    @staticmethod
    def generate_bill(user_id):
        cart_dict = db.reference("Users/{}/cart".format(user_id)).get()
        actual_amount = 0
        for key,values in cart_dict.items():
            actual_amount += int(values['Price'])
        
        # delete all the  elements from cart
        db.reference("Users/{}/cart".format(user_id)).delete()

        # returning total amount
        return actual_amount

    @staticmethod
    def remove_product_from_cart(product):

        pass

