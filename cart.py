from firebase import firebase
from firebase_admin import db

class Cart:

    def __init__(self, user_id=None, items=None, discount=None, total_amount=None):
        self.user_id = user_id
        self.items = items
        self.discount = discount
        self.total_amount = total_amount

    def add_user_to_cart(self, user_id=None, items=None, discount=None, total_amount=None):

        data = {
            'UserID': user_id,
            'Items': items,
            'Discount': discount,
            'Total Amount': total_amount,
        }

        new_ref = db.reference('Cart').push(data)
        return new_ref.key


    @staticmethod
    def remove_from_cart(id):
        db.reference("Cart/{}".format(id)).delete()
        print("Bill Paid. Cart Empty !!")

    @staticmethod
    def get_cart_by_cart_id(cart_id):
        cart = db.reference("Cart/{}".format(cart_id)).get()
        return cart

    @staticmethod
    def get_cart_by_user_id(user_id):
        pass
