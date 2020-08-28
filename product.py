from firebase import firebase
from firebase_admin import db

class Product:

    def __init__(self, name=None, company=None, about=None, specification=None, category=None, category_id=None):
        self.name = name
        self.company = company
        self.about = about
        self.specification = specification
        self.category = category
        self.category_id = category

    def add_product(self,name, company, about="Inches", specification="RAM ROM", category="Appliances", category_id=None):

        data = {
            'Name': name,
            'Company': company,
            'About': about,
            'Specification': specification,
            'Category': category,
            'Category_ID': category_id,
        }

        new_ref = db.reference('Product').push(data)
        print(new_ref.key)


    @staticmethod
    def remove_product(id):
        db.reference("Product/{}".format(id)).delete()

    @staticmethod
    def show_products():
        products = db.reference("Product").get()
        return products


# product_object = Product()
# product_id = product_object.add_product("DEll", "Dell")

# remove_product(id)
# show_products()
