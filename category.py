from firebase import firebase
from firebase_admin import db

from prettytable import PrettyTable

class Category:

    def __init__(self, category_name=None):
        self.category_name = category_name

    def add_category(self, category_name=None):
        data = {
            'category_name': category_name, 
        }

        new_ref = db.reference('Category').push(data)
        return new_ref.key

    @staticmethod
    def remove_category(id):
        db.reference("Category/{}".format(id)).delete()

    @staticmethod
    def get_all_categories():
        categories = db.reference("Category").get()

        print("All Categories:")
        count = 1

        t = PrettyTable(["S.no", "Category"])
        if categories:
            for category_id, values in categories.items():
                t.add_row([count, values['category_name']])
                count += 1
            print(t)
            return True
        else:
            t.add_row([0, "No Category !!"])
            print(t)
            return False


    @staticmethod
    def get_category_by_id(id):
        category = db.reference("Category/{}".format(id)).get()
        return category
