from model.Data import UsFo

    
def test_test_add_user(app):
    app.user.Add_user(UsFo(firstname="привет", middlename="привет", lastname="привет", nickname="привет", title="привет", company="привет", address="привет", home="привет", mobile="привет", work="привет", fax="привет", email="привет", email2="привет", email3="привет", homepage="привет", yearbirt="1989", yearanni="1989", address2="привет", phone2="привет", notes="привет"))

def test_test_add_empty_user(app):
    app.user.Add_user(UsFo(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", yearbirt="", yearanni="", address2="", phone2="", notes=""))


