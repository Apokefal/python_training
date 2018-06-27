from model.Data import UsFo
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [UsFo(firstname="", lastname="", address="", homephone="",
                 mobilephone="", workphone="", secondaryphone="", email="", email2="",
                 email3="")] + [
    UsFo(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), address=random_string("address", 20),
         homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10),
         workphone=random_string("workphone", 20), secondaryphone=random_string("secondaryphone", 20),
         email=random_string("email1", 10), email2=random_string("email2", 10), email3=random_string("email3", 10))
    for i in range(5)]

@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
    
def test_test_add_user(app, user):
    old_users = app.user.get_user_list()
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

