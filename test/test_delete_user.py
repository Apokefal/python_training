##
from model.Data import UsFo


def test_delete_user(app):
    if app.user.counts() == 0:
        app.user.Add_user(UsFo(firstname="test"))
    old_users = app.user.get_user_list()
    app.user.delete_first_user()
    assert len(old_users) - 1 == app.user.counts()
    new_users = app.user.get_user_list()
    old_users[0:1] = []
    assert old_users == new_users
