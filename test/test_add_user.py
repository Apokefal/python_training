from model.Data import UsFo


def test_test_add_user(app, db, check_ui):
    user = json_users
    old_users = db.get_user_list()
    app.user.Add_user(user)
    new_users = db.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=UsFo.id_or_max) == sorted(new_users, key=UsFo.id_or_max)


#def test_test_add_empty_user(app):
#    old_users = app.user.get_user_list()
#    user = UsFo(firstname="при2вет", middlename="при123вет", lastname="1")
#    app.user.Add_user(user)
#    assert len(old_users) + 1 == app.user.counts()
#    new_users = app.user.get_user_list()
#    old_users.append(user)
#    assert sorted(old_users, key=UsFo.id_or_max) == sorted(new_users, key=UsFo.id_or_max)

