import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from product import Product
from category import Category
from users import Users
from bill import Bill

from customer import customer_start
from admin import admin_start


cred = credentials.Certificate("mycart-python-firebase-authenticate-key.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mycart-python.firebaseio.com/'
})


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
        customer_start()
    elif choice in 'aA':
        print("Hello Admin!!")
        admin_start() 
    else:
        print("Wrong Choice !!! Please try again")

    pass
    # exit


starting()