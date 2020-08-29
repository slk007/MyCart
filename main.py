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


logged_in_user_id = None

def search_user_for_login(email, password, boolean_admin):

    users_dic = Users.get_all_users()

    for user_id,value in users_dic.items():
        if value['admin_boolean'] == boolean_admin and value['email']==email and value['password']==password:
            print("Welcome" , value['name'])

            global logged_in_user_id
            logged_in_user_id = user_id

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

    global logged_in_user_id
    logged_in_user_id = new_user_id

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

def print_product_by_id(id):
    product = Product.get_product_by_id(id)
    print("Name :", product['Name'])
    print("Category :", product['Category'])
    print("Company :", product['Company'])
    print("Specification :", product['Specification'])
    print("Price :", product['Price'])
    print("-"*30)

def print_products_by_category(category_name):
    product_id_list = Product.get_products_id_by_category_name(category_name)
    for product_id in product_id_list:
        print_product_by_id(product_id)

def show_bill(bill):
    print("-"*30)
    print("-"*13, "BILL", "-"*13)
    print("Date:", bill['Date'])
    print("Actual Amount: ", bill['Actual Amount'])
    print("Discount: -", bill['Discount'])
    print("-"*10)
    print("Final Amount: ", bill['Final Amount'])
    print("-"*30)

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
    if print_products_by_category(category_choice):
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

# category
    # view category list
    Category.get_all_categories()

    # select category
    print("Type the Category You Want to Select:")
    print("-"*30)
    category_choice = input("Your Choice :")
    print("-"*30)


# product
    # view product list per category
    if print_products_by_category(category_choice):
        print("-"*30)
    else:
        print("-"*30)

    # view product by name
    print("Type the Product Name You Want to Add to Cart:")
    print("-"*30)
    product_choice = input("Your Choice :")

    # add product to cart
    u = Users()
    u.add_to_cart(logged_in_user_id, Product.get_product_by_id(Product.get_product_id_by_product_name(product_choice)))

    # view cart
    Users.view_cart(logged_in_user_id)

    # shop more

    # generate bill
    print("Do you want to checkout cart now? y/n?")
    choice = input("Generate Bill : ")

    actual_amount = 0
    if choice:
        actual_amount = Users.generate_bill(logged_in_user_id)

    # pay bill    
    billing = Bill()
    bill_id = billing.add_bill(userid=logged_in_user_id, actual_amount=actual_amount)

    bill_object = Bill.get_bill_by_id(bill_id)
    show_bill(bill_object)

    print("Thanks for Shopping !!!")

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

