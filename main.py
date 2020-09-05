# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

from db import db_obj

from product import Product
from category import Category
from users import Users
from bill import Bill
import admin

from customer import customer_start
from admin import admin_start

from prettytable import PrettyTable


def start_mycart():
    
    # initiatating firebase certificate

    print("-"*30)
    print("Welcome to MyCart !!!!!!!")
    print("-"*30)
    print("Shop for above Rs.10,000 and avail an instant discount of Rs.500\nHurry Up !!!!!!!!!!11")
    print("-"*30)

    while True:

        t = PrettyTable(["MyCart Menu", "Type"])
        t.add_row(["Customer", "c/C"])
        t.add_row(["Admin", "a/A"])
        t.add_row(["Exit", "e/E"])
        print(t)

        choice = input("\nYour Choice: ")
        
        print("-"*30)
        
        if len(choice) == 1:
            if choice in 'eE':
                # exit
                print("See you soon !!")
                exit()

            elif choice in 'cC':
                # takes you to customer.py
                print("Let's Shop!!")
                customer_start()

            elif choice in 'aA':
                # take you to admin.py
                print("Hello Admin!!")
                admin_start()
            else:
                # go to while loop again
                print("Wrong Choice !!! Please try again")    
        else:
            # go to while loop again
            print("Please type only 1 character !!! Try again.")
    


# our MyCart takes off from here
start_mycart()


