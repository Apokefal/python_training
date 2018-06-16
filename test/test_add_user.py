from model.Data import UsFo

    
def test_test_add_user(app):
    old_users = app.user.get_user_list()
    user = UsFo(firstname="при2вет", middlename="при123вет", lastname="привrwtrtет")
    app.user.Add_user(user)
    new_users = app.user.get_user_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=UsFo.id_or_max) == sorted(new_users, key=UsFo.id_or_max)


def test_test_add_empty_user(app):
    old_users = app.user.get_user_list()
    user = UsFo(firstname="при2вет", middlename="при123вет", lastname="привrwtrtет", nickname="привет", title="привет", company="привет", address="привет", home="привет", mobile="привет", work="привет", fax="привет", email="привет", email2="привет", email3="привет", homepage="привет", yearbirt="1989", yearanni="1989", address2="привет", phone2="привет", notes="привет")
    app.user.Add_user(user)
    new_users = app.user.get_user_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=UsFo.id_or_max) == sorted(new_users, key=UsFo.id_or_max)

