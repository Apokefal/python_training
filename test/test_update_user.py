###
from model.Data import UsFo
import random

def test_update_some_user(app, db, check_ui):
    user = UsFo(firstname="test", lastname="test", id="1",address="test", homephone="test", mobilephone="test", workphone="test", secondaryphone="test", email="test@gmail.com")
    if len(db.get_user_list()) == 0:
        app.user.Add_user(UsFo(firstname="W"))
    old_users = db.get_user_list()
    random_user = random.choice(old_users)
    app.user.Edit_user_by_id(random_user.id, user)
    new_users = db.get_user_list()
    user.id = random_user.id
    old_users.remove(random_user)
    old_users.append(user)
    assert len(old_users) == len(new_users)
    if check_ui:
        assert sorted(new_users, key=UsFo.id_or_max) == sorted(app.user.get_user_list(), key=UsFo.id_or_max)
