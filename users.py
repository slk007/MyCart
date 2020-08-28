from firebase import firebase

class Users:

    global fb
    fb = firebase.FirebaseApplication("https://mycart-python.firebaseio.com/", None)

    def __init__(self, firstname=None, lastname=None, email=None, admin_boolean=False):

        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.admin_boolean = admin_boolean

    def add_user(self, firstname, lastname, email="abce@gmail.com", admin_boolean=False):

        data = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'admin_boolean': admin_boolean
        }
        result = fb.post('/Users', data)
        print("User created with id: ", result)

    def show_users(self):
        result = fb.get('/Users', '')
        print(result)

# users_object = Users()
# users_object.add_user("new", "user")
