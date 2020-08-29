from firebase_admin import auth

def creating_authenticted_users():

    user = auth.create_user(
        email='user@example.com',
        email_verified=False,
        phone_number='+15555550100',
        password='secretPassword',
        display_name='John Doe',)
    print('Sucessfully created new user: {0}'.format(user.uid))

creating_authenticted_users()