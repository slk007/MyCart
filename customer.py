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


def print_product_by_id(id):
    product = Product.get_product_by_id(id)
    print("Name :", product['Name'])
    print("Category :", product['Category'])
    print("Company :", product['Company'])
    print("Specification :", product['Specification'])
    print("Price :", product['Price'])
    print("-"*30)

def print_bill(bill):
    print("-"*30)
    print("-"*13, "BILL", "-"*13)
    print("Date:", bill['Date'])
    print("Actual Amount: ", bill['Actual Amount'])
    print("Discount: -", bill['Discount'])
    print("-"*10)
    print("Final Amount: ", bill['Final Amount'])
    print("-"*30)


def customer_start():

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
    print_bill(bill_object)

    print("Thanks for Shopping !!!")

    # exit
    pass
