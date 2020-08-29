from firebase import firebase
from firebase_admin import db

class Product:

    def __init__(self):
        self.name = None
        self.company = None
        self.about = None
        self.specification = None
        self.category = None
        self.category_id = None

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

    @staticmethod
    def get_product_id_by_product_name(product_name):
        product_dic = db.reference("Product").order_by_child("Name").equal_to(product_name).get()
        product_id = ""    
        for key,value in product_dic.items():
            product_id = key
        return product_id

    @staticmethod
    def get_products_id_by_category_name(category_name):
        product_dic = db.reference("Product").order_by_child("Category").equal_to(category_name).get()
        product_id_list = []
        for key,value in product_dic.items():
            product_id_list.append(key)
        return product_id_list
