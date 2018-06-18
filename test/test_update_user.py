##
from model.Data import UsFo

def test_update_user(app):
    if app.user.counts() == 0:
        app.user.Add_user(UsFo(firstname="W"))
    old_users = app.user.get_user_list()
    user = UsFo(firstname="W", lastname="A")
    user.id = old_users[0].id
    app.user.Edit_user(user)
    assert len(old_users) == app.user.counts()
    new_users = app.user.get_user_list()
    old_users[0] = user
    assert sorted(old_users, key=UsFo.id_or_max) == sorted(new_users, key=UsFo.id_or_max)
