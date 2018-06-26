##
from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name=name
        self.header=header
        self.footer=footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return  (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize




class UsFo:
    def __init__(self, firstname=None, lastname=None, address=None, homephone=None, mobilephone=None,
                 workphone=None, secondaryphone=None, email=None, id=None):
        self.firstname=firstname
        self.lastname=lastname
        self.address=address
        self.home=homephone
        self.mobile=mobilephone
        self.work=workphone
        self.email=email
        self.phone2=secondaryphone
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize



