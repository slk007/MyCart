from firebase import firebase

class Category:

    global fb
    fb = firebase.FirebaseApplication("https://mycart-python.firebaseio.com/", None)

    def __init__(self, category_name=None):
        self.category_name = category_name

    def add_category(self, category_name=None):
        data = {
            'category_name': category_name,
        }
        result = fb.post('/Category', data)
        print("Category created with id: ", result)

    def remove_category(self, id):

        fb.delete('/Category', id)
        print("Deleted")

    def show_categories(self):
        result = fb.get('/Category', '')
        print(type(result))

# category_object = Category()
# category_object.add_category("Clothes")
# category_object.remove_category()
