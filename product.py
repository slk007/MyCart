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

    def add_product(self, name, company, about, specification, category, price):

        data = {
            'Name': name,
            'Company': company,
            'About': about,
            'Specification': specification,
            'Category': category,
            'Price': price,
        }

        new_ref = db.reference('Product').push(data)
        return new_ref.key


    @staticmethod
    def remove_product(id):
        db.reference("Product/{}".format(id)).delete()
        print("Deleted !!")

    @staticmethod
    def get_all_products():
        products = db.reference("Product").get()
        return products

    @staticmethod
    def get_products_per_category(category):
        all_products = db.reference("Product").get()

        if all_products:
            dic = {}
            for product_id, value in all_products.items():
                if value['Category'] == category:
                    dic[product_id] = value
            return dic
        else:
            print("No Products for this categroy yet !!")
            return False

    
    @staticmethod
    def get_product_by_id(id):
        product = db.reference("Product/{}".format(id)).get()
        return product


# product_object = Product()
# product_id = product_object.add_product("DEll", "Dell")

# remove_product(id)
# get_all_products()
# get_product_by_id(id)
