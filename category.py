from firebase import firebase
from firebase_admin import db

class Category:

    def __init__(self, category_name=None):
        self.category_name = category_name

    def add_category(self, category_name=None):
        data = {
            'category_name': category_name, 
        }

        new_ref = db.reference('Category').push(data)
        print(new_ref.key)

    @staticmethod
    def remove_category(id):
        db.reference("Category/{}".format(id)).delete()

    @staticmethod
    def show_categories():
        categories = db.reference("Category").get()
        return categories
        

# category_object = Category()
# category_object.add_category("Clothes")
# category_object.remove_category()
