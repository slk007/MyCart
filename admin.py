from product import Product
from category import Category
from users import Users
from bill import Bill

from prettytable import PrettyTable

import getpass

logged_in_admin_id = None
selected_user_id = None
selected_customer_id = None

from firebase_admin import db

from db import db_obj, Db


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


def new_category():
    print("-"*30)
    print("Please Enter New Category Name : ")
    new_cat = input("Category : ")

    ref_var = db.reference('Category').order_by_child('category_name').equal_to(new_cat).get()

    if ref_var:
        return False
    category_object = Category()
    new_category_id = category_object.add_category(new_cat)
    return new_cat



def print_users(users_dic):
    print("-"*12, "USERS", "-"*13)

    if users_dic:
        count = 1
        t = PrettyTable(["S.No", "User Name"])
        for key, value in users_dic.items():
            if value['admin_boolean'] == False:
                t.add_row([count, value['name']])
                count += 1
        print(t)
        return True
    else:
        return False


def handling_customers():

    while True:
        print("Type s/S to select a customer, any other to go back?")
        wanna_select = input("Your Choice : ")

        if wanna_select not in "sS":
            return

        print("Type the name of the Customer, to view his cart/bills :")
        selected_customer_name = input("Customer Name : ")

        global selected_customer_id
        selected_customer_id = Users.get_user_id_by_user_name(selected_customer_name)


        t = PrettyTable(["Customer Options", "Type"])
        t.add_row(["Cart", 'c/C'])
        t.add_row(["Bills", 'b/B'])
        t.add_row(["Return Back", 'r/R'])
        print(t)

        choice = input("Your Choice : ")

        if len(choice) == 1:

            if choice in "cC":
                # show cart by user(customer) id
                print("Cart of Selected Customer:")
                c =  Users.view_cart(selected_customer_id)
                
            elif choice in "bB":
                # show bills by user(customer) id
                print("Bills of Selected Customer:")
                bills_id_list = Bill.get_bills_by_user_id(selected_customer_id)
                Db.print_bills(bills_id_list)

            elif choice in "rR":
                return
            else:
                print("Wrong Choice!!! Try Again.")
                continue
        else:
            print("Choice should be of 1 char !!! Try Again.")
            continue
    return

def handling_products(category_choice):

    while True:
        product_present = print_products_by_category(category_choice)

        t = PrettyTable(["Product Menu", "Type"])
        t.add_row(["New Product", "n/N"])
        if product_present:
            t.add_row(["Remove Product", "r/R"])
        t.add_row(["Back", "b/B"])
        print(t)

        print("-"*30)
        choice = input("Your Choice : ")
        print("-"*30)

        if len(choice) == 1:
            if choice in 'n/N':
                # new product
                print('-'*30)
                print("Enter Details for new Product:")
                print('-'*30)

                product_name = input("Product Name : ")

                ref_var = db.reference("Product").order_by_child('Name').equal_to(product_name).get()

                if ref_var:
                    print("Product Already Exists")
                    continue
                product_company = input("Product Company : ")
                product_about = input("Product About : ")
                product_specs = input("Product Specifications : ")
                product_price = input("Price : ")

                prod_object = Product()
                prod_id = prod_object.add_product(name=product_name, company=product_company, about=product_about, specification=product_specs, category=category_choice, price=product_price)

            elif choice in 'rR':
                # remove product
                print('-'*30)
                print("Enter Product Name to be Delete")
                print('-'*30)
                product_name = input("Product Name:")
                Product.remove_product(Product.get_product_id_by_product_name(product_name))
            elif choice in "bB":
                return
            else:
                print("Wrong Choice!!! Try Again")
                continue
        else:
            print("Please select one character only !!! Try Again")
            continue
    return



def handling_category():

    while True:
        print("-"*30)
        c = Category.get_all_categories()

        t = PrettyTable(["Category Menu", "Type"]) 
        if c:
            t.add_row(["Select a Category", "s/S"])
        t.add_row(["Create New Category", "n/N"])
        t.add_row(["Return Back", "b/B"])
        print(t)

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
                handling_products(category_choice)

            elif choice in 'nN':
                # add category
                category_choice = new_category()
                if category_choice:
                    handling_products(category_choice)
                else:
                    print("Category Already Exists!! Try Another")
                    continue
            elif choice in "bB":
                return
            else:
                print("Type only one character. Try Again!!!")
                continue
        else:
            print("Wrong Choice. Please Try again")
            continue
    return


def admin_handles():

    while True:

        t = PrettyTable(["Admin Menu", "Type"])
        t.add_row(["View Customers", "v/V"])
        t.add_row(["Catergories", "c/C"])
        t.add_row(["<-- Back to User Menu", "b/B"])
        print(t)

        choice = input("\nYour Choice: ")

        print("-"*30)

        if len(choice) == 1:
            if choice in 'vV':
                # view all customer
                users_dict = Users.get_all_users()

                if print_users(users_dict):

                    # showing their bills and cart
                    handling_customers()
                else:
                    # when no user added yet
                    continue

            elif choice in 'cC':
                # add remove category
                handling_category()

            elif choice in 'bB':
                return
            else:
                print("Wrong Choice!!! Try Again.")
                continue
        else:
            print("Choice should be of 1 char !!! Try Again.")
            continue
    return



def admin_start():

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

                # create admin
                current_admin_id = db_obj.sign_up(True)

                if current_admin_id:
                    admin_handles()
                else:
                    print("Admin with same email/name already exists!!!! Try Again")
                    print("-"*30)
                    return

            elif choice in 'lL':
                # login
                try:
                    current_admin_id = db_obj.login(True)
                    if current_admin_id:
                        admin_handles()
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
