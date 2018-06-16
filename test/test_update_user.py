from model.Data import UsFo

def test_update_user(app):
    if app.user.counts() == 0:
        app.user.Add_user(UsFo(firstname="W"))
    old_users = app.user.get_user_list()
    app.user.Edit_user(UsFo(firstname="W", middlename="A", company="L", address="E", home="R", mobile="K", work="O"))
    new_users = app.user.get_user_list()
    assert len(old_users) == len(new_users)
