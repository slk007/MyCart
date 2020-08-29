from firebase import firebase
from firebase_admin import db

from datetime import date

class Bill:

    def __init__(self, userid=None, invoice=None, date=None, items=None, discount=0, paid_amount=0):
        self.userid = userid
        self.invoice = invoice
        self.date = date
        self.items = items
        self.discount = discount
        self.paid_amount = paid_amount

    def add_bill(self, userid=None, invoice=None, items=None, total_amount=0, discount=0, paid_amount=0):

        data = {
            'UserID': userid,
            'Invoice': invoice,
            'Date': str(date.today()),
            'Items': items,
            'Total Amount': total_amount,
            'Discount': discount,
            'Paid Amount': paid_amount,
        }

        new_ref = db.reference('Bill').push(data)
        return new_ref.key


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
        pass