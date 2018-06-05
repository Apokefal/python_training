from model.Data import Group

def test_update_group_name(app):
    app.session.Login(username="admin", password="secret")
    app.group.Edit_first_group(Group(name="New group"))
    app.session.Logout()

def test_update_group_header(app):
    app.session.Login(username="admin", password="secret")
    app.group.Edit_first_group(Group(header="New header"))
    app.session.Logout()