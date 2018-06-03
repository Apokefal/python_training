from model.Data import Group

def test_update_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.Edit_group(Group(name="test", header="test", footer="test"))
    app.session.Logout()
