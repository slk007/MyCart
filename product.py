from firebase import firebase

class Product:

    global fb
    fb = firebase.FirebaseApplication("https://mycart-python.firebaseio.com/", None)

    def __init__(self, name=None, company=None, about=None, specification=None, category=None, category_id=None):
        self.name = name
        self.company = company
        self.about = about
        self.specification = specification
        self.category = category
        self.category_id = category

    def add_product(self,name, company, about="Inches", specification="RAM ROM", category="Appliances", category_id=None):
        # fb = firebase.FirebaseApplication("https://mycart-python.firebaseio.com/", None)
        data = {
            'Name': name,
            'Company': company,
            'About': about,
            'Specification': specification,
            'Category': category,
            'Category_ID': category_id,
        }
        result = fb.post('/Product', data)
        print("Product created with id: ", result)
        return result[name]

    def remove_product(self, id):
        # fb = firebase.FirebaseApplication("https://mycart-python.firebaseio.com/", None)
        fb.delete('/Product', id)
        print("deleted")

    def show_products(self):
        result = fb.get('/Product', '')
        print(result)


product_object = Product()
# product_id = product_object.add_product("Vostro", "Dell")
# product_object.remove_product(id)
product_object.show_products()
