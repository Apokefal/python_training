from model.Data import Group
from model.Data import UsFo
from fixture.orm import ORMFixture
import random

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_user_in_group(app, db):
    if len(db.get_user_list()) == 0:
        app.user.Add_user(UsFo(firstname="Apok", lastname="Efal", id="1",address="Tomsk", homephone="88005553535",
                               mobilephone="88002000600", workphone="83823563822",
                               secondaryphone="89609777888", email="test@gmail.com"))
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="Test"))
        user_list = db.get_user_list()
        random_user = random.choice(user_list)
        group_list_db = db.get_group_list()
        random_group = random.choice(group_list_db)
        app.user.add_to_group(user_id=random_user.id, group_id=random_group.id)
        users_in_group = orm.get_users_in_group(random_group)
        for user in users_in_group:
            if user.id == random_user.id:
                assert True