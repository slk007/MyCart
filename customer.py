from product import Product
from category import Category
from users import Users
from bill import Bill

from prettytable import PrettyTable

import getpass

logged_in_user_id = None

def search_user_for_login(email, password, boolean_admin):

    users_dic = Users.get_all_users()
    user_id = None
    for user_id,value in users_dic.items():
        if value['admin_boolean'] == boolean_admin and value['email']==email and value['password']==password:
            print("Welcome" , value['name'])

            global logged_in_user_id
            logged_in_user_id = user_id

            break
    print("-"*30)
    return user_id


def sign_up(boolean_admin):
    print("To Sign Up Please Enter Below Details:")

    name = input("Name: ")
    email_id = input("Email: ")
    password = getpass.getpass("Password: ")

    new_user = Users()
    new_user_id = new_user.add_user(name, email_id, password, boolean_admin)

    print("Sign Up Successfull !!")

    global logged_in_user_id
    logged_in_user_id = new_user_id

    return new_user_id


def login(boolean_admin):
    print("To Login Please Enter Below Details:")

    email = input("Email: ")
    password = getpass.getpass("Password: ")
    print("-"*30)

    return search_user_for_login(email, password, boolean_admin)


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
    t = PrettyTable(["Invoice Number", "1"])
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

        t = PrettyTable(["Invoice Number", "1"])
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
        t.add_row(["Checkout & Buy", "b/B"])
        t.add_row(["<--Return to Customer Menu", "r/R"])
        print(t)

        choice = input("\nYour Choice: ")

        if len(choice) == 1:
            if choice in 'bB':
                    
                # generate bill
                print("Do you want to checkout cart now? y/n?")
                choice = input("Generate Bill : ")
                    
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

            elif choice in 'rR':
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

def category_interaction():

    while True:
        # view category list
        cat_present = Category.get_all_categories()

        if cat_present:

            print("Wanna select any Category? y/n")
            want_cat = input("Your Choice : ")

            if want_cat in "yY":
                # select category
                print("Type Category You Want to Select:")
                print("-"*30)
                category_choice = input("Your Choice : ")
                print("-"*30)
            
            else:
                # go back to user menu
                return


            # product
            # view product list per category
            if print_products_by_category(category_choice):

                print("Wanna buy any product from the above list ? y/n")
                wanna_buy = input("Your Choice : ")

                if wanna_buy in 'yY':

                    # select product by name
                    print("Type the 'Product Name' You Want to Add to Cart:")
                    print("-"*30)
                    product_choice = input("Your Choice : ")

                    # add product to cart
                    u = Users()
                    u.add_to_cart(logged_in_user_id, Product.get_product_by_id(Product.get_product_id_by_product_name(product_choice)))
                    return
                else:
                    continue

            else:
                print("No such product present")
                return

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
                continue
        else:
            print("Type 1 character only!! Try again")
            continue
    return


def customer_start():

    while True:

        t = PrettyTable(["User Menu", "Type"])
        t.add_row(["Sign Up", "s/S"])
        t.add_row(["Log IN", "l/L"])
        t.add_row(["<--Back to MyCart Menu", "b/B"])
        print(t)

        choice = input("\nYour Choice: ")
        print("-"*30)

        if len(choice) == 1:
            if choice in 'sS':
                # create account
                current_user_id = sign_up(False)
                if current_user_id:
                    customer_carting()

            elif choice in 'lL':
                # login
                current_user_id = login(False)
                if current_user_id:
                    customer_carting()

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
