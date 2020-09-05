from product import Product
from users import Users
from bill import Bill
from db import db_obj
import unittest


class SimpleTest(unittest.TestCase):

    def test_login(self):
        print("Running Test Case to check if user is already present ....")
        v = db_obj.find_user_in_db("shantanu", "shantanu")
        self.assertEqual(v, True)

    def test_products_for_category_name(self):
        print("\nTesting if products id can be determined using prodcut name ....")
        v = Product.get_product_id_by_product_name("Sauce")
        self.assertIsNot(v, False)

    def test_products_per_category(self):
        print("\nTesting if products can be found using category name .....")
        v = Product.get_products_id_by_category_name("Food")
        self.assertIsNot(v, False)

    def test_user_id_by_user_name(self):
        print("\nTesting if we can get user id by using user name .....")
        v = Users.get_user_id_by_user_name("mayank")
        self.assertIsNot(v, False)

    def test_user_bill_by_user_id(self):
        print("\nGettings user bill by user id .....")
        v = Bill.get_bills_by_user_id("-MFxtrAItwAq4gANvU1X")
        self.assertIsNot(v, False)


if __name__ == '__main__':
    unittest.main()
