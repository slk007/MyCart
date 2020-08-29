from product import Product
from category import Category
from users import Users
from bill import Bill

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



def print_products_by_category(category_name):
    product_id_list = Product.get_products_id_by_category_name(category_name)
    for product_id in product_id_list:
        print_product_by_id(product_id)



def new_category():
    print("-"*30)
    print("Please Enter New Category:")
    new_cat = input("Category : ")

    category_object = Category()
    new_category_id = category_object.add_category(new_cat)
    return new_cat

def print_bill(bill):
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
    print(users_dict = Users.get_all_users())
    
    # see his order details or bill
    print("Type the name of the User, to view his cart/bills :")
    bill_choice = input("User Name:")



    # exit
    pass