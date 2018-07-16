from datetime import datetime
from pony.orm import *
from pymysql.converters import encoders, decoders, convert_mysql_timestamp
from model.Data import UsFo
from model.Data import Group


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        users = Set(lambda: ORMFixture.ORMUser, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMUser(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        homephone = Optional(str, column='home')
        mobilephone = Optional(str, column='mobile')
        workphone = Optional(str, column='work')
        secondaryphone = Optional(str, column='phone2')
        deprecated = Optional(str, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    def __init__(self, host, name, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=conv)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_user_list(self):
        return self.convert_users_to_model(select(c for c in ORMFixture.ORMUser if c.deprecated is None))

    def convert_users_to_model(self, users):
        def convert(user):
            return UsFo(id=str(user.id), firstname=user.firstname, lastname=user.lastname,
                        address=str(user.address), email=user.email, email2=user.email2, email3=user.email3,
                        homephone=user.homephone, workphone=user.workphone,
                        mobilephone=user.mobilephone, secondaryphone=user.secondaryphone,
                        all_phones_from_home_page=None, all_emails_from_home_page=None)
        return list(map(convert, users))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_user_list(self):
        return self.convert_users_to_model(select(u for u in ORMFixture.ORMUser if u.deprecated is None))

    @db_session
    def get_users_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_users_to_model(
            select(u for u in ORMFixture.ORMUser if u.deprecated is None and orm_group not in u.groups))

    @db_session
    def get_users_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_users_to_model(
            select(u for u in ORMFixture.ORMUser if u.deprecated is None and orm_group not in u.groups))