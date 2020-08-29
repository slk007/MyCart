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
        return new_ref.key

    @staticmethod
    def remove_category(id):
        db.reference("Category/{}".format(id)).delete()

    @staticmethod
    def get_all_categories():
        categories = db.reference("Category").get()

        if categories:

            print("-"*30)
            print("All Categories")
            print("-"*30)

            for category_id, values in categories.items():
                print(values['category_name'])
                
            print("-"*30)
            return True
        else:
            print("Sorry No Categories Yet !!!")
            print("-"*30)
            return False


    @staticmethod
    def get_category_by_id(id):
        category = db.reference("Category/{}".format(id)).get()
        return category
        

# category_object = Category()
# category_object.add_category("Clothes")
# category_object.remove_category()
