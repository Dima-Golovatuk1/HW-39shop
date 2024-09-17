from data import get_user

class UserLogin():
    def fromdb(self, user_id, db):
        self.__user = db(user_id)
        return self

    def create(self, user):
        self.__user = user
        return self

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymomus(self):
        return False

    def get_id(self):
        return str(self.__user[0])