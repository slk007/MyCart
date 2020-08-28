import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from product import Product
from category import Category
from users import Users

cred = credentials.Certificate("mycart-python-firebase-authenticate-key.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mycart-python.firebaseio.com/'
})



# db.reference("/Product").get())
# Product.show_products()
# print("-----------------------")
# Product.remove_product('-MFpfd9Yx2sP49VduHMO')
# print("-----------------------")
# Product.show_products()
# new_product_obj = Product()
# new_product_obj.add_product("Lenivo", "lelo")

# print(Category.show_categories())
# Category.remove_category("-MFoxyV7M7o1hqPJYw_4")

# print(Users.show_users())