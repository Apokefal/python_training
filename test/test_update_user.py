from model.Data import UsFo

def test_update_user(app):
    app.user.Edit_user(UsFo(firstname="test", middlename="test", lastname="test", nickname="test", title="test", company="test", address="test", home="test", mobile="test", work="test", fax="test", email="test", email2="test", email3="test", homepage="test", yearbirt="1989", yearanni="1989", address2="test", phone2="test", notes="test"))
