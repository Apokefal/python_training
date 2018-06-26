from model.Data import UsFo

    
def test_test_add_user(app):
    old_users = app.user.get_user_list()
    user = UsFo(firstname="при2вет", lastname="привrwtrtет")
    app.user.Add_user(user)
    assert len(old_users) + 1 == app.user.counts()
    new_users = app.user.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=UsFo.id_or_max) == sorted(new_users, key=UsFo.id_or_max)


def test_test_add_empty_user(app):
    old_users = app.user.get_user_list()
    user = UsFo(firstname="при2вет", lastname="привrwtrtет")
    app.user.Add_user(user)
    assert len(old_users) + 1 == app.user.counts()
    new_users = app.user.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=UsFo.id_or_max) == sorted(new_users, key=UsFo.id_or_max)

