from product import Product
from category import Category
from users import Users
from bill import Bill

from prettytable import PrettyTable

import getpass

from firebase_admin import db

logged_in_user_id = None


def sign_up(boolean_admin):
    print("To Sign Up Please Enter Below Details:")

    name = input("Name: ")
    email_id = input("Email: ")
    password = getpass("Password : ")

    r1, r2 = None, None
    r1 = dict(db.reference('Users').order_by_child('name').equal_to(name).get())
    r2 = dict(db.reference('Users').order_by_child('email').equal_to(email_id).get())

    if r1 or r2:
        raise Exception("User Already Exists !!!")

    new_user = Users()
    new_user_id = new_user.add_user(name, email_id, password, boolean_admin)

    print("Sign Up Successfull !!")

    global logged_in_user_id
    logged_in_user_id = new_user_id

    return new_user_id


def login(boolean_admin):

    global logged_in_user_id
    print("To Login Please Enter Below Details : ")

    email = input("Email: ")
    password = getpass.getpass("Password: ")
    
    r = None
    r = dict(db.reference('Users').order_by_child('email').equal_to(email).get())

    if r:
        if password == r[list(r.keys())[0]]['password']:
            logged_in_user_id = list(r.keys())[0]
            return list(r.keys())[0]

    raise Exception("Credentials Wrong!!")


def print_product_by_id(id):
    product = Product.get_product_by_id(id)
    t = PrettyTable(["Name", product['Name']])
    t.add_row(["Category", product['Category']])
    t.add_row(["Company", product['Company']])
    t.add_row(["Specification", product['Specification']])
    t.add_row(["Price", product['Price']])
    print(t)


def print_products_by_category(category_name):
    product_id_list = Product.get_products_id_by_category_name(category_name)

    print("All Products for '{}' category:".format(category_name))

    if product_id_list:
        for product_id in product_id_list:
            print_product_by_id(product_id)
        return True
    else:
        return False


def print_bill(bill):
    print("-"*40)
    print("-"*13, "BILL", "-"*13)
    t = PrettyTable(["Invoice Number", bill["Invoice"]])
    t.add_row(["Date", bill['Date']])
    t.add_row(["Actual Amount", bill['Actual Amount']])
    t.add_row(["Discount", bill['Discount']])
    t.add_row(["Final Amount", bill['Final Amount']])
    print(t)
    print("-"*40)


def print_bills(bills):
    print("-"*40)
    print("All Bills are here:")
    for bill_id in bills:
        bill = Bill.get_bill_by_id(bill_id)

        t = PrettyTable(["Invoice Number",  bill["Invoice"]])
        t.add_row(["Date", bill['Date']])
        t.add_row(["Actual Amount", bill['Actual Amount']])
        t.add_row(["Discount", bill['Discount']])
        t.add_row(["Final Amount", bill['Final Amount']])
        print(t)
    print("-"*40)



def handling_cart():

    items_present = Users.view_cart(logged_in_user_id)

    if items_present:

        t = PrettyTable(["Cart Menu", "Type"])
        t.add_row(["Checkout & Buy", "c/C"])
        t.add_row(["<--Back to Customer Menu", "b/B"])
        print(t)

        choice = input("\nYour Choice: ")

        if len(choice) == 1:
            if choice in 'cC':
                    
                # generate bill
                print("Do you want to checkout cart now? ")
                tb = PrettyTable(["Cart Menu", "Type"])
                tb.add_row(["Yes", "y/Y"])
                tb.add_row(["No", "n/N"])
                print(tb)

                choice = input("Generate Bill : ")
                print("-"*30)
                    
                if choice in "yY":
                    actual_amount = 0
                    actual_amount = Users.generate_bill(logged_in_user_id)

                    print("You will be paying Rs.{} ................".format(actual_amount))
                    yes_no = input("Pay : ")

                    # pay bill    
                    billing = Bill()
                    bill_id = billing.add_bill(userid=logged_in_user_id, actual_amount=actual_amount)

                    bill_object = Bill.get_bill_by_id(bill_id)
                    print_bill(bill_object)

                    print("Thanks for Shopping !!!")
                else:
                    return

            elif choice in 'bB':
                return
            else:
                print("Wrong Choice. Please Try again")
                return
        else:
            print("Type 1 character only!! Try again")
            return
    else:
        print("Empty Cart.\nShop Now !! And get discount upto Rs.500!!\nHurry!!!!!!!!!!")

        # put category link here
        return



def product_interaction(category_choice):

    while True:
        # view product list per category
        if print_products_by_category(category_choice):

            print("Select product from the above list ?")
            t = PrettyTable(["Product Menu", "Type"])
            t.add_row(["Yes", "y/Y"])
            t.add_row(["No", "n/N"])
            print(t)

            wanna_buy = input("Your Choice : ")
            print("-"*30)

            if wanna_buy in 'yY':

                # select product by name
                print("Type 'Product Name' You Want to Add to Cart:")
                print("-"*30)
                product_choice = input("Your Choice : ")
                print("-"*30)

                if not db.reference("Product").order_by_child('Name').equal_to(product_choice).get():
                    print("No such Product Exists")
                    print("-"*30)
                    continue

                # add product to cart
                u = Users()
                u.add_to_cart(logged_in_user_id, Product.get_product_by_id(Product.get_product_id_by_product_name(product_choice)))
                return

            elif wanna_buy in "nN":
                return
            else:
                print("Type one char only!!! Try again.")
                print("-"*30)
                continue

        else:
            print("No products for this category.")
            return
    return




def category_interaction():

    while True:
        # view category list
        cat_present = Category.get_all_categories()

        if cat_present:

            print("Select any Category from the above list ?")
            tb = PrettyTable(["Category Menu", "Type"])
            tb.add_row(["Yes", "y/Y"])
            tb.add_row(["No", "n/N"])
            print(tb)

            want_cat = input("Your Choice : ")
            print("-"*30)

            if want_cat in "yY":
                # select category
                print("Type Category You Want to Select:")
                print("-"*30)
                category_choice = input("Your Choice : ")
                print("-"*30)

                if not db.reference('Category').order_by_child('category_name').equal_to(category_choice).get():
                    print("No such category exits !!!! Try Again")
                    continue
            
            elif want_cat in "nN":
                # go back to user menu
                return
            else:
                print("Type one character only!! Try Again")
                print("-"*30)
                continue

            # product
            product_interaction(category_choice)


        else:
            return

    return

def customer_carting():
    
    while True:

        t = PrettyTable(["Customer Menu", "Type"])
        t.add_row(["Product Categories", "p/P"])
        t.add_row(["Cart", "C/c"])
        t.add_row(["Bills", "b/B"])
        t.add_row(["<-- Return to User Menu", "r/R"])
        print(t)

        choice = input("\nYour Choice: ")
        print("-"*30)

        if len(choice) == 1:
            if choice in 'pP':
                # show categories then products
                category_interaction()
                
            elif choice in 'cC':
                # handling cart
                handling_cart()

            elif choice in 'bB':
                # show bills
                bills_id_list = Bill.get_bills_by_user_id(logged_in_user_id)
                if bills_id_list:
                    print_bills(bills_id_list)
                else:
                    print("No Bills Yet !!\nShop Now.\nAvail Discount Upto Rs.500")
                    continue

            elif choice in 'rR':
                return

            else:
                print("Wrong Choice. Please Try again")
                print("-"*30)
                continue
        else:
            print("Type 1 character only!! Try again")
            print("-"*30)
            continue
    return


def customer_start():

    while True:

        t = PrettyTable(["User Menu", "Type"])
        t.add_row(["Signup", "s/S"])
        t.add_row(["Login", "l/L"])
        t.add_row(["<--Back to MyCart Menu", "b/B"])
        print(t)

        choice = input("\nYour Choice: ")
        print("-"*30)

        if len(choice) == 1:
            if choice in 'sS':
                # create account
                try:
                    current_user_id = sign_up(False)
                    if current_user_id:
                        customer_carting()
                except Exception:
                    print("User with same email/name already exists!!!! Try Again")
                    print("-"*30)
                    return

            elif choice in 'lL':
                # login
                try:
                    current_user_id = login(False)
                    if current_user_id:
                        customer_carting()
                except Exception:
                    print("Wrong Credentials!!!! Try Again")
                    print("-"*30)
                    return

            elif choice in 'b/B':
                return

            else:
                print("Wrong Choice. Please Try again")
                continue
        else:
            print("Type 1 character only!! Try again")
            continue

    # exit
    return
