import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from product import Product
from category import Category
from users import Users
from bill import Bill
from cart import Cart

cred = credentials.Certificate("mycart-python-firebase-authenticate-key.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mycart-python.firebaseio.com/'
})



def search_user_for_login(email, password, boolean_admin):

    users_dic = Users.get_all_users()

    for user_id,value in users_dic.items():
        if value['admin_boolean'] == boolean_admin and value['email']==email and value['password']==password:
            print("Welcome" , value['name'])
            break

    print("-"*30)

def sign_up(boolean_admin):
    print("To Sign Up Please Enter Below Details:")

    name = input("Name: ")
    email_id = input("Email: ")
    password = input("Password: ")

    new_user = Users()
    new_user_id = new_user.add_user(name, email_id, password, boolean_admin)

    print("Sign Up Successfull !!")
    print(new_user_id)


def login(boolean_admin):
    print("To Login Please Enter Below Details:")

    email = input("Email: ")
    password = input("Password: ")

    return search_user_for_login(email, password, boolean_admin)


def new_category():
    print("-"*30)
    print("Please Enter New Category:")
    new_cat = input("Category : ")

    category_object = Category()
    new_category_id = category_object.add_category(new_cat)

    return new_cat

def products_per_category(category_name):
    products_per_cat = Product.get_products_per_category(category_name)
    if products_per_cat:
        for key,value in products_per_cat.items():
            print("Name:", value['Name'],'\n', "Company:", value['Company'],'\n',"About:", value['About'],'\n',"Specification:", value['Specification'],'\n',"Category:", value['Category'])
            print("-"*10)
        return True
    else:
        return False

def product_by_name():
    print(Product.get_product_by_name('Dell'))


def admin_start():

    print("-"*30)
    print("Type 'l/L' for Login")
    print("Type 's/S' for SignUp")
    print("Type 'e/E' for Exit")
    print("-"*30)
    choice = input("Your Choice : ")
    print("-"*30)

    if len(choice) == 1:
        if choice in 'sS':
            # create account
            current_user_id = sign_up(True)

        elif choice in 'lL':
            # login
            current_user_id = login(True)

    else:
        print("Wrong Choice. Please Try again")

# category part

    # view category list
    print("-"*30)
    if Category.get_all_categories():
        print("Type 's/S' to Select a Category")
    
    print("Type 'n/N' to Create New Category")
    print("-"*30)
    choice = input("Your Choice : ")
    print("-"*30)

    category_choice = ""

    if len(choice) == 1:
        if choice in 'sS':
            # select category
            print("Type the Category You Want to Select:")
            print("-"*30)
            category_choice = input("Your Choice : ")
            print("-"*30)

        elif choice in 'nN':
            # add category
            category_choice = new_category()

    else:
        print("Wrong Choice. Please Try again")


# product part

    # show products list per category
    if products_per_category(category_choice):
        print("Type 'r/R' to Remove Product")

    print("Type 'n/N' to Add New Product")
    print("-"*30)
    choice = input("Your Choice : ")
    print("-"*30)

    # product_choice = ""

    if len(choice) == 1:
        if choice in 'n/N':
            # new product
            print('-'*30)
            print("Enter Details for new Product:")
            print('-'*30)

            product_name = input("Product Name : ")
            product_company = input("Product Company : ")
            product_about = input("Product About : ")
            product_specs = input("Product Specifications : ")
            product_price = input("Price : ")


            prod_object = Product()
            prod_id = prod_object.add_product(name=product_name, company=product_company, about=product_about, specification=product_specs, category=category_choice, price=product_price)
            

        elif choice in 'rR':
            # remove product
            print('-'*30)
            print("Enter Product ID to be Delete")
            print('-'*30)
            product_id = input("Product ID:")
            Product.remove_product(product_id)


    # users part
    print("-"*30)
    print("Users List:")
    print("-"*30)

    # see users list
    users_dict = Users.get_all_users()
    

    # see his order details or bill

    # exit
    pass

def user_start():

    print("-"*30)
    print("Type 'l/L' for Login")
    print("Type 's/S' for SignUp")
    print("Type 'e/E' for Exit")
    print("-"*30)
    choice = input("Your Choice : ")
    print("-"*30)

    if len(choice) == 1:
        if choice in 'sS':
            # create account
            current_user_id = sign_up(False)

        elif choice in 'lL':
            # login
            current_user_id = login(False)

    else:
        print("Wrong Choice. Please Try again")


    # view category list
    print(Category.get_all_categories())

    # select category
    print("Type the Category You Want to Select:")
    print("-"*30)
    category_choice = input("Your Choice :")
    print("-"*30)

    # view product list per category
    if products_per_category(category_choice):
        print("-"*30)
    else:
        print("-"*30)

    # view product by name

    # add product to cart

    # return back to product list

    # shop more

    # generate bill

    # pay bill

    # exit
    pass


def starting():

    print("-"*30)
    print("Welcome to MyCart")
    print("-"*30)
    print("Type c/C if you are a Customer")
    print("Type a/A if you are Admin")
    print("Type e/E to exit application")
    print("-"*30)
    choice = input("Your Choice: ")
    print("-"*30)
    
    if choice in 'eE':
        print("See you soon!")
    elif choice in 'cC':
        print("Let's Shop!!")
        user_start()
    elif choice in 'aA':
        print("Hello Admin!!")
        admin_start()
    else:
        print("Wrong Choice !!! Please try again")

    pass


starting()


# bill_object = Bill()
# print(bill_object.add_bill('userid', 123456, {'Laptop':20000}, 25000, 500, 24500))

# cart_obj = Cart()
# print(cart_obj.add_user_to_cart("-MFtSESHPtEX3oFRp1nJ", {'Plant':500}, 0, 500))

# print(Cart().show_cart_by_id('-MFuKkIAZgxohVtGqYnl'))

# print(Users.get_user_by_id('-MFtSESHPtEX3oFRp1nJ'))

# p = Product()

# print(p.add_product(name="Mouse", company="Boat", about="Black", specification="Wired", category="Gadgets", price="900"))