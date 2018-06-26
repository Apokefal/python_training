from model.Data import UsFo

    
def test_test_add_user(app):
    old_users = app.user.get_user_list()
    user = UsFo(firstname="при2вет", lastname="привrwtrtет", id="1", homephone="89609451", workphone="435345435", mobilephone="64651651651", secondaryphone="3243243243")
    app.user.Add_user(user)
    app.user.Open_home_page()
    assert len(old_users) + 1 == app.user.counts()
    new_users = app.user.get_user_list()
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

