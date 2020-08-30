from firebase import firebase
from firebase_admin import db

from datetime import date

class Bill:

    def __init__(self):
        self.userid = None
        self.username = None
        self.invoice = None
        self.date = None
        self.actual_amount = None
        self.discount = None
        self.final_amount = None

    def add_bill(self, userid=None, username=None, invoice=None, discount=0, actual_amount=0):

        if actual_amount > 10000:
            discount = 500
        final_amount = actual_amount - discount

        data = {
            'UserID': userid,
            'Username': username,
            'Invoice': invoice,
            'Date': str(date.today()),
            'Actual Amount': actual_amount,
            'Discount': discount,
            'Final Amount': final_amount,
        }
        new_ref = db.reference('Bill').push(data)
        return new_ref.key

    @staticmethod
    def get_bill_by_id(id):
        bill = db.reference("Bill/{}".format(id)).get()
        return bill

    @staticmethod
    def remove_bill(id):
        db.reference("Bill/{}".format(id)).delete()
        print("Deleted !!")

    @staticmethod
    def get_all_bills():
        all_bills = db.reference("Bill").get()
        return all_bills

    @staticmethod
    def get_bills_by_user_id(user_id):
        bill_dic = db.reference("Bill").order_by_child("UserID").equal_to(user_id).get()
        bill_id_list = []
        for key,value in bill_dic.items():
            bill_id_list.append(key)
        return bill_id_list
