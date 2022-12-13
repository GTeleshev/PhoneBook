import dbconnect
class Entry:

    def __init__(self, lastname = '', firstname= '', phone = '', description = ''):
        self.lastname = lastname
        self.firstname = firstname
        self.phone = phone
        self.description = description

    def printentry(self):
        print(self.lastname, self.firstname, self.phone, self.description)

    def add_db(self):
        dbconnect.insert(self.lastname, self.firstname, self.phone, self.description)

    def get_id(self):
        user_tuple = dbconnect.select_full(self.lastname, self.firstname, self.phone, self.description)
        id = user_tuple[0][0]
        return id
