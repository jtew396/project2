from flask_login import UserMixin

# Flask Login User Model
class User(UserMixin):
    number_of_users = 0
    user_database = {}

    def __init__(self):
        User.number_of_users += 1
        id = self.number_of_users
        self.id = id
        self.name = "user" + str(id)
        self.display_name = self.name
        User.user_database[self.id] = {
            'name': self.name,
            'display_name': self.display_name
        }
        # self.password = self.name + "_secret"


    def __repr__(self):
        return "%d/%s" % (self.id, self.name)
        # return "%d/%s/%s" % (self.id, self.name, self.password)

    @classmethod
    def get(cls, id):
        return cls.user_database.get(id)
