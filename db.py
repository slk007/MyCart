import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import getpass

from bill import Bill

from prettytable import PrettyTable

class Db:

    def initiating_firebase_app(self):
        """ Function certifies the  """

        self.cred = credentials.Certificate("mycart-python-firebase-authenticate-key.json")

        firebase_admin.initialize_app(self.cred, {
            'databaseURL': 'https://mycart-python.firebaseio.com/'
        })

    def __init__(self):

        self.initiating_firebase_app()

        self.ref_users = db.reference("Users")
        self.ref_bill = db.reference("Bill")
        self.ref_category = db.reference("Category")
        self.ref_products = db.reference("Product")

        self.user_id = None
        self.admin_id = None


    def get_bills_by_user_id(self):
        bill_dic = self.ref_bill.order_by_child("UserID").equal_to(self.user_id).get()
        bill_id_list = []
        for key,value in bill_dic.items():
            bill_id_list.append(key)
        return bill_id_list


    @staticmethod
    def print_bill(bill):
        print("-"*13, "BILL", "-"*13)
        t = PrettyTable(["Invoice Number", bill["Invoice"]])
        t.add_row(["Date", bill['Date']])
        t.add_row(["Actual Amount", bill['Actual Amount']])
        t.add_row(["Discount", bill['Discount']])
        t.add_row(["Final Amount", bill['Final Amount']])
        print(t)

    @staticmethod
    def print_bills(bills):
        print("-"*40)
        print("All Bills are here:")
        for bill_id in bills:
            bill = Bill.get_bill_by_id(bill_id)
            Db.print_bill(bill)
        print("-"*40)


    def find_user_in_db(self, name, email_id):
        # searching for user in db

        r1, r2 = None, None
        r1 = dict(self.ref_users.order_by_child('name').equal_to(name).get())
        r2 = dict(self.ref_users.order_by_child('email').equal_to(email_id).get())

        if r1 or r2:
            return True
        else:
            return False

    
    def adding_new_user(self, name, email_id, password, boolean_admin):
        
        return Users().add_user(name, email_id, password, boolean_admin)


    def sign_up(self, boolean_admin):

        print("To Sign Up Please Enter Below Details:")

        name = input("Name: ")
        email_id = input("Email: ")
        password = getpass("Password : ")

        # checking if user already present
        user_present = Db.find_user_in_db(name, email_id)

        if user_present:
            # user is already present hence can't sign up
            return False
        else: 
            # user is not present
            # creating new user if not present
            self.user_id = adding_new_user(name, email_id, password, boolean_admin)

            if boolean_admin:
                # admin
                self.admin_id, self.user_id = self.user_id, None
                print("Sign Up Successfull !!")
                return self.admin_id
            else:
                # normal user or customer
                print("Sign Up Successfull !!")
                return self.user_id
        

    def login(self, boolean_admin):

        print("To Login Please Enter Below Details : ")

        email = input("Email: ")
        password = getpass.getpass("Password: ")
        
        r = None
        r = dict(self.ref_users.order_by_child('email').equal_to(email).get())
        
        if r:
            temp = list(r.keys())[0] 
            if password == r[temp]['password']:
                if boolean_admin:
                    # admin
                    self.admin_id = temp
                else:
                    # normal user or customer
                    self.user_id = temp
                print("-"*30)
                print("Welcome {} !!!".format(email))
                return temp

        raise Exception("Credentials Wrong!!")


db_obj = Db()
