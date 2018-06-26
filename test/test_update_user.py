###
from model.Data import UsFo
from random import randrange

def test_update_some_user(app):
    if app.user.counts() == 0:
        app.user.Add_user(UsFo(firstname="W"))
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    user = UsFo(firstname="W", lastname="A")
    user.id = old_users[index].id
    app.user.Edit_user_by_index(index, user)
    assert len(old_users) == app.user.counts()
    new_users = app.user.get_user_list()
    old_users[index] = user
    assert sorted(old_users, key=UsFo.id_or_max) == sorted(new_users, key=UsFo.id_or_max)
