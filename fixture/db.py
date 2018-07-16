import pymysql.cursors
from model.Data import Group
from model.Data import UsFo
###
class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.username = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)


    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_user_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, home, mobile, work, phone2 \
                           from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, homephone, mobilephone, workphone, secondaryphone) = row
                list.append(
                    UsFo(id=str(id), firstname=firstname, lastname=lastname,
                         address=address,  email=email,
                         homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone,
                         all_emails_from_home_page=None, all_phones_from_home_page=None))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()