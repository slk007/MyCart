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

    def add_product(self, name, company, about="", specification="", category="Appliances", category_id=None, price=0):

        data = {
            'Name': name,
            'Company': company,
            'About': about,
            'Specification': specification,
            'Category': category,
            'Category_ID': category_id,
            'Price': price,
        }

        new_ref = db.reference('Product').push(data)
        return new_ref.key


    @staticmethod
    def remove_product(id):
        db.reference("Product/{}".format(id)).delete()
        print("Deleted !!")

    @staticmethod
    def show_all_products():
        products = db.reference("Product").get()
        return products

    @staticmethod
    def show_products_per_category(category):
        all_products = db.reference("Product").get()
        dic = {}
        for product_id, value in all_products.items():
            if value['Category'] == category:
                dic[product_id] = value

        return dic

    # @staticmethod
    # def show_product_by_name(name):
    #     snapshot = db.reference("Product").order_by_child('Name').get()
    #     for key, val in snapshot.items():
    #         print('{0} was {1} meters tall'.format(key, val))


# product_object = Product()
# product_id = product_object.add_product("DEll", "Dell")

# remove_product(id)
# show_products()
