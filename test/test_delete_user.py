##
from model.Data import UsFo
from random import randrange

def test_delete_user(app):
    if app.user.counts() == 0:
        app.user.Add_user(UsFo(firstname="test"))
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    app.user.delete_user_by_index(index)
    assert len(old_users) - 1 == app.user.counts()
    new_users = app.user.get_user_list()
    old_users[index:index+1] = []
    assert old_users == new_users
